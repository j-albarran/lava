#!/bin/bash

cd /opt/ltp

# EMMC
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_100M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_10M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_100M"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_S_FUNC_DD_RW_QUICK"
./runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_M_FUNC_DD_RW_20TIMES"

# GPIO
./runltp -P beaglebone-black -f ddt/gpio-tests -s "GPIO_S_FUNC_DIR_IN_ALL_BANK"

# MEMORY
./runltp -P beaglebone-black -f ddt/memtest -s "MEMORY_M_FUNC_MEMTESTER_10pct_1time"

# CRYPTO
./runltp -P beaglebone-black -f ddt/crypto_aes -s "CRYPTO_S_PERF_AES"

# PWM
./runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_00"
./runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_50"

# IPC
#################./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

# SCHEDULER
#################./runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K"

# USBHOST
./runltp -P beaglebone-black -f ddt/usbhost_dd_rw_vfat -s "USBHOST_S_FUNC_VFAT_DD_RW_0007"
./runltp -P beaglebone-black -f ddt/usbhost_dd_rw_ext2 -s "USBHOST_M_FUNC_EXT2_DD_RW_0007"

# ALSA
./runltp -P beaglebone-black -f ddt/alsa_samplerate -s "ALSA_S_FUNC_PLAYBACK_SMPRT_44100"

# MMC
./runltp -P beaglebone-black -f ddt/mmc_sdhccard_dd_rw_vfat -s "MMC_S_FUNC_SDHC_VFAT_DD_RW_512K"
./runltp -P beaglebone-black -f ddt/mmc_sdhccard_dd_rw_vfat -s "MMC_S_FUNC_SDHC_VFAT_DD_RW_50M"
./runltp -P beaglebone-black -f ddt/mmc_parallel_processing -s "MMC_S_FUNC_MULTI_THREAD_READWRITE"
./runltp -P beaglebone-black -f ddt/mmc_dd_rw -s "MMC_S_FUNC_DD_RW_QUICK"
./runltp -P beaglebone-black -f ddt/mmc_dd_rw -s "MMC_M_FUNC_DD_RW_20TIMES"

# FBDEV
./runltp -P beaglebone-black -f ddt/fbdev_disp -s "FBDEV_XS_FUNC"

# ETH
./runltp -P beaglebone-black -f ddt/eth_ping -s "ETH_S_FUNC_PING_300S"
./runltp -P beaglebone-black -f ddt/eth_ping -s "ETH_S_FUNC_MULTI_INTERFACE_PING_DOWN"

# RTC
./runltp -P beaglebone-black -f ddt/rtc_readtime -s "RTC_S_FUNC_READTIME_0001"
./runltp -P beaglebone-black -f ddt/rtc_setgettime -s "RTC_S_FUNC_SETGETTIME_0001"

# I2C
./runltp -P beaglebone-black -f ddt/i2c_detect -s "I2C_S_FUNC_I2CDETECT"

# WDT
./runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_SETTIMEOUT"
./runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETBOOTSTATUS"
./runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETSTATUS"
./runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETTIMEOUT"
./runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETSUPORT"

# POWERMGR
./runltp -P beaglebone-black -f ddt/powermgr_cpufreq -s "POWERMGR_S_FUNC_CPUFREQ_BASIC"
./runltp -P beaglebone-black -f ddt/powermgr_dyn_tcks -s "POWERMGR_S_FUNC_DYNAMIC_TICKS"
./runltp -P beaglebone-black -f ddt/powermgr_suspend -s "POWERMGR_S_FUNC_SIMPLE_SUSPEND"
./runltp -P beaglebone-black -f ddt/powermgr_suspend -s "POWERMGR_S_FUNC_SIMPLE_STANDBY"

# TIMERS
#################./runltp -P beaglebone-black -f ddt/mmc_dd_rw -s "MMC_M_FUNC_DD_RW_20TIMES"
