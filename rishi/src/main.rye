//! The `rishi` command-line tool — the first version of the Rishi shell.
//!
//! Rishi is the shell of the Rye ecosystem: terse for the hand, typed for
//! safety, a sibling of Rye that shares its value model. This first version is
//! honest about how small it is. It reads a `.rish` script and runs it
//! directly, supporting line comments, `let` bindings of strings and integers,
//! and `say` with `${name}` interpolation. It is the seed from which the
//! language grows toward `parity.rish`, the program that will name its first
//! real purpose (see active-designing/996_growing_a_language.md).
//!
//! Rishi is implemented in Rye and built against Rye's own standard library, so
//! the language we are growing and the language we build it in are one and the
//! same — and a value here is, in time, a value there.
//!
//! Commands:
//!   rishi version          Print the Rishi version.
//!   rishi run <file.rish>  Read and run a single .rish script.

const std = @import("std");

/// Rishi's version, stamped chronologically — YYYYMMDD.HHMMSS, where later is
/// larger, the same clock Rye keeps. This is Rishi's founding stamp.
const rishi_version = "20260618.175012";

/// A Rishi value. The first two kinds — a string and an integer — are the seed
/// of a model that will grow to lists, records, and process results, shared
/// with Rye so a value can cross between them without a seam.
const Value = union(enum) {
    string: []const u8,
    int: i64,

    fn write(self: Value) void {
        switch (self) {
            .string => |s| std.debug.print("{s}", .{s}),
            .int => |x| std.debug.print("{d}", .{x}),
        }
    }
};

const Binding = struct { name: []const u8, value: Value };

/// A bounded environment of name-to-value bindings. Bounded on purpose: the
/// limit is stated, so a runaway script meets a clear edge rather than eating
/// memory without end.
const Env = struct {
    items: [256]Binding = undefined,
    count: usize = 0,

    fn bind(self: *Env, name: []const u8, value: Value) !void {
        std.debug.assert(self.count <= self.items.len);
        if (self.count == self.items.len) return error.TooManyBindings;
        self.items[self.count] = .{ .name = name, .value = value };
        self.count += 1;
    }

    /// Look a name up, most-recent binding first, so a later `let` shadows an
    /// earlier one of the same name.
    fn lookup(self: *const Env, name: []const u8) ?Value {
        var i = self.count;
        while (i > 0) {
            i -= 1;
            if (std.mem.eql(u8, self.items[i].name, name)) return self.items[i].value;
        }
        return null;
    }
};

pub fn main(init: std.process.Init) !u8 {
    const arena = init.arena.allocator();
    const args = try init.minimal.args.toSlice(arena);
    if (args.len < 2) {
        printUsage();
        return 0;
    }

    const command = args[1];
    if (std.mem.eql(u8, command, "version")) {
        std.debug.print("rishi {s}  (chronological: YYYYMMDD.HHMMSS, later is larger)\n", .{rishi_version});
        return 0;
    } else if (std.mem.eql(u8, command, "run")) {
        return runFile(init, args);
    } else if (std.mem.eql(u8, command, "help") or std.mem.eql(u8, command, "--help")) {
        printUsage();
        return 0;
    } else {
        std.debug.print("rishi: unknown command '{s}'\n\n", .{command});
        printUsage();
        return 2;
    }
}

fn printUsage() void {
    std.debug.print(
        \\rishi {s} — the shell of the Rye ecosystem (first version)
        \\
        \\usage:
        \\  rishi version          print the Rishi version
        \\  rishi run <file.rish>  read and run a single .rish script
        \\
    , .{rishi_version});
}

fn runFile(init: std.process.Init, args: []const [:0]const u8) !u8 {
    const arena = init.arena.allocator();
    const io = init.io;

    if (args.len < 3) {
        std.debug.print("rishi run: expected a .rish file\n", .{});
        return 2;
    }
    const path = args[2];

    // A `.rish` script is required; reject the negative space plainly.
    if (!std.mem.endsWith(u8, path, ".rish")) {
        std.debug.print("rishi run: script must end with .rish, got '{s}'\n", .{path});
        return 2;
    }

    const dir = std.Io.Dir.cwd();
    const source = dir.readFileAlloc(io, path, arena, .unlimited) catch |err| {
        std.debug.print("rishi run: could not read '{s}': {s}\n", .{ path, @errorName(err) });
        return 1;
    };

    return interpret(source);
}

/// Run a Rishi script, line by line. Returns 0 when the whole script runs, or 1
/// at the first line that does not make sense — named with its line number, so
/// the trouble is easy to find.
fn interpret(source: []const u8) u8 {
    var env = Env{};
    var line_no: usize = 0;
    var lines = std.mem.splitScalar(u8, source, '\n');
    while (lines.next()) |raw| {
        line_no += 1;
        const line = std.mem.trim(u8, raw, " \t\r");
        if (line.len == 0 or line[0] == '#') continue;
        evalStatement(&env, line) catch |err| {
            std.debug.print("rishi: line {d}: {s}\n  {s}\n", .{ line_no, @errorName(err), line });
            return 1;
        };
    }
    return 0;
}

fn evalStatement(env: *Env, line: []const u8) !void {
    if (std.mem.startsWith(u8, line, "let ")) {
        const rest = std.mem.trim(u8, line[4..], " \t");
        const eq = std.mem.indexOfScalar(u8, rest, '=') orelse return error.LetNeedsEquals;
        const name = std.mem.trim(u8, rest[0..eq], " \t");
        const valstr = std.mem.trim(u8, rest[eq + 1 ..], " \t");
        if (name.len == 0) return error.LetNeedsName;
        try env.bind(name, try parseValue(valstr));
    } else if (std.mem.startsWith(u8, line, "say ")) {
        try doSay(env, std.mem.trim(u8, line[4..], " \t"));
    } else {
        return error.UnknownStatement;
    }
}

/// A value literal is a double-quoted string or a base-ten integer.
fn parseValue(s: []const u8) !Value {
    if (s.len >= 2 and s[0] == '"' and s[s.len - 1] == '"') {
        return .{ .string = s[1 .. s.len - 1] };
    }
    const x = std.fmt.parseInt(i64, s, 10) catch return error.ValueMustBeStringOrInt;
    return .{ .int = x };
}

/// `say` writes a string literal — interpolating `${name}` as it goes — or the
/// value bound to a bare name, then a newline.
fn doSay(env: *const Env, arg: []const u8) !void {
    if (arg.len >= 2 and arg[0] == '"' and arg[arg.len - 1] == '"') {
        const inner = arg[1 .. arg.len - 1];
        var i: usize = 0;
        while (i < inner.len) {
            if (i + 1 < inner.len and inner[i] == '$' and inner[i + 1] == '{') {
                const close = std.mem.indexOfScalarPos(u8, inner, i + 2, '}') orelse return error.UnterminatedInterpolation;
                const name = inner[i + 2 .. close];
                const value = env.lookup(name) orelse return error.UndefinedName;
                value.write();
                i = close + 1;
            } else {
                // Print the literal run up to the next '$' (or the end). The
                // single-character step keeps a lone '$' moving forward.
                const next = std.mem.indexOfScalarPos(u8, inner, i, '$') orelse inner.len;
                const stop = if (next > i) next else i + 1;
                std.debug.print("{s}", .{inner[i..stop]});
                i = stop;
            }
        }
        std.debug.print("\n", .{});
    } else if (arg.len > 0) {
        const value = env.lookup(arg) orelse return error.UndefinedName;
        value.write();
        std.debug.print("\n", .{});
    } else {
        return error.SayNeedsArgument;
    }
}
