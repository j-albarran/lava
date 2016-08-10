#!/usr/bin/python

import re
import sys
import os

def runtests():
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_640K" 2>&1 | tee output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw_vfat -s "EMMC_S_FUNC_VFAT_DD_RW_100M" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_10M" 2>&1 | tee -a output.txt')
    os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw_ext2 -s "EMMC_S_FUNC_EXT2_DD_RW_100M" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_S_FUNC_DD_RW_QUICK" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/emmc_dd_rw -s "EMMC_M_FUNC_DD_RW_20TIMES" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/gpio-tests -s "GPIO_S_FUNC_DIR_IN_ALL_BANK" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/memtest -s "MEMORY_M_FUNC_MEMTESTER_10pct_1time" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/crypto_aes -s "CRYPTO_S_PERF_AES" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_00" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/pwm_backlight -s "PWM_S_FUNC_BACKLIGHT_50" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/usbhost_dd_rw_vfat -s "USBHOST_S_FUNC_VFAT_DD_RW_0007" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/usbhost_dd_rw_ext2 -s "USBHOST_M_FUNC_EXT2_DD_RW_0007" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/alsa_samplerate -s "ALSA_S_FUNC_PLAYBACK_SMPRT_44100" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/mmc_sdhccard_dd_rw_vfat -s "MMC_S_FUNC_SDHC_VFAT_DD_RW_512K" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/mmc_sdhccard_dd_rw_vfat -s "MMC_S_FUNC_SDHC_VFAT_DD_RW_50M" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/mmc_parallel_processing -s "MMC_S_FUNC_MULTI_THREAD_READWRITE" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/mmc_dd_rw -s "MMC_S_FUNC_DD_RW_QUICK" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/mmc_dd_rw -s "MMC_M_FUNC_DD_RW_20TIMES" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/fbdev_disp -s "FBDEV_XS_FUNC" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/eth_ping -s "ETH_S_FUNC_PING_300S" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/eth_ping -s "ETH_S_FUNC_MULTI_INTERFACE_PING_DOWN" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/rtc_readtime -s "RTC_S_FUNC_READTIME_0001" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/rtc_setgettime -s "RTC_S_FUNC_SETGETTIME_0001" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/i2c_detect -s "I2C_S_FUNC_I2CDETECT" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_SETTIMEOUT" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETBOOTSTATUS" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETSTATUS" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETTIMEOUT" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/wdt_test -s "WDT_S_FUNC_GETSUPORT" 2>&1 | tee -a output.txt')
    os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/powermgr_cpufreq -s "POWERMGR_S_FUNC_CPUFREQ_BASIC" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/powermgr_dyn_tcks -s "POWERMGR_S_FUNC_DYNAMIC_TICKS" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/powermgr_suspend -s "POWERMGR_S_FUNC_SIMPLE_SUSPEND" 2>&1 | tee -a output.txt')
    #os.system('/opt/ltp/runltp -P beaglebone-black -f ddt/powermgr_suspend -s "POWERMGR_S_FUNC_SIMPLE_STANDBY" 2>&1 | tee -a output.txt')

def results():
    pattern = re.compile("^(?!.+ED)(?P<test_case_id>\\w+)\\s+(?P<result>PASS|FAIL)\\s+\\d+")
    f = open("output.txt", "r")
    try:
       for line in f:
          for parser in [pattern]:
              result = parser.search(line)
              if result is not None:
                 if parser is pattern:
                    test_id = result.group('test_case_id')
        	    test_result = result.group('result')
                    os.system('lava-test-case %s --result %s' % (test_id, test_result.lower()))
       sys.exit(0)
    finally: f.close()
    print "ERROR: Parser failed and ran to EOF"
    sys.exit(1)

runtests()
results()
