#!/bin/bash

cd /opt/ltp

./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_100M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_10M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_100M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_S_FUNC_DD_RW_QUICK"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_M_FUNC_DD_RW_20TIMES"

./runltp -P beaglebone-black -f ddt/gpio-tests -s "GPIO_S_FUNC_DIR_IN_ALL_BANK"

./runltp -P beaglebone-black -f ddt/memtest -s "MEMORY_M_FUNC_MEMTESTER_10pct_1time"

./runltp -P beaglebone-black -f ddt/crypto_aes -s "CRYPTO_S_PERF_AES"

./runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_00"
./runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_50"

#################./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
#./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
