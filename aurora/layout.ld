/* aurora/seed.ld — where Aurora's first seed lives in memory.
 *
 * QEMU's `virt` machine begins executing at the base of RAM, 0x8000_0000, so we
 * lay the seed down there and make `_start` the entry. The `.text.init` section
 * holds `_start` and is placed first, so the very first instruction the machine
 * runs is the one that gives the hart its stack. */
ENTRY(_start)
SECTIONS {
  . = 0x80000000;
  .text : { KEEP(*(.text.init)) *(.text*) }
  .rodata : { *(.rodata*) }
  .data : { *(.data*) }
  .bss : { *(.bss*) }
}
