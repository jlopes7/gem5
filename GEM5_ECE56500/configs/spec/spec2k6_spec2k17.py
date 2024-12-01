# Title: spec2k6_spec2k17.py
# Author: Conor Green
# Purpose: Benchmarks for SafeBet project
# Description: Modification of spec2k6 script which helps parse
#       which benchmark and creates a process. Spec2k6 partys are
#       heavily based on Melek Musleh's spec2k6 code,
#       the copyright is given below.
# Usage: Call through get_process() from another script


# Copyright (c) 2012 Purdue University
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Malek Musleh

### The following file was referenced from the following site:
### http://www.m5sim.org/SPEC_CPU2006_benchmarks
###
### and subsequent changes were made


import os
import optparse
import sys
import shutil

import m5
from m5.objects import Process, buildEnv

m5.util.addToPath('../common')

def check_spec2k17(options):
    sp = ["s", "fs", "is", "r"]
    if any("_"+x in options.benchmark for x in sp):
       return True
    return False

def get_process(options, target_isa="arm"):

    # default
    process = Process()

    ### SPEC 2006
    # X86 binary path
    #bench_dir_06='/home/yara/mithuna2/green456/SPEC_2006/benchspec/CPU2006/'
    #exe_dir_06 = '/home/yara/mithuna2/green456/SPEC_2006/benchspec/CPU2006/'

    # ARM binary path
    bench_dir_06='/home/min/a/ece565/benchspec-2020/CPU2006/'
    exe_dir_06='/home/min/a/ece565/benchspec-2020/CPU2006/'
    exe_suffix = '_base.amd64-armcross'
    if("x86" in target_isa):
      exe_suffix = '_base.amd64-m64-gcc43-nn'

    ### SPEC 2017
    # X86 binaries
    output_dir = '/tmp/'
    bench_dir_17 = '/home/yara/mithuna2/green456/benchmark_sources/'\
                   'SPEC-OSG-2021/SPEC_2017/benchspec/CPU/'
    if(check_spec2k17(options)):
      exe_suffix = '_base.spectre_safebet-m64'

    # refrate process definitions unfinished (3 were started)
    refrate_run_dir = 'run/run_base_refrate_spectre_safebet-m64.0000/'

    refspeed_run_dir = 'run/run_base_refspeed_spectre_safebet-m64.0000/'

    ## Floating Point Speed

    # 603 bwaves_s
    bwaves_s = Process()
    bwaves_s_dir = '603.bwaves_s/'
    bwaves_s_run_dir = bwaves_s_dir + refspeed_run_dir
    bwaves_s.executable = bench_dir_17 + bwaves_s_run_dir\
	 + 'speed_bwaves' + exe_suffix
    bwaves_s_data = 'bwaves_1.in'
    bwaves_s.cmd = [bwaves_s.executable]
    bwaves_s.output = 'bwaves_s.out'
    bwaves_s.input = bench_dir_17 + bwaves_s_run_dir + bwaves_s_data

    # 607 cactuBSSN_s
    cactuBSSN_s = Process()
    cactuBSSN_s_dir = '607.cactuBSSN_s/'
    cactuBSSN_s_run_dir = cactuBSSN_s_dir + refspeed_run_dir
    cactuBSSN_s.executable = bench_dir_17 + cactuBSSN_s_run_dir+\
	 'cactuBSSN_s' + exe_suffix
    cactuBSSN_s_data = 'spec_ref.par'
    cactuBSSN_s.cmd = [cactuBSSN_s.executable] + [cactuBSSN_s_data]
    cactuBSSN_s.output = 'cactuBSSN_s.out'
    cactuBSSN_s.cwd = bench_dir_17 + cactuBSSN_s_run_dir

    # 619 lbm_s
    lbm_s = Process()
    lbm_s_dir = '619.lbm_s/'
    lbm_s_run_dir = lbm_s_dir + refspeed_run_dir
    lbm_s.executable = bench_dir_17 + lbm_s_run_dir + 'lbm_s' + exe_suffix
    lbm_s_data = '200_200_260_ldc.of'
    lbm_s.cmd = [lbm_s.executable] +\
	 ['2000', 'reference.dat','0','0',lbm_s_data]
    lbm_s.output = 'lbm_s.out'
    lbm_s.cwd = bench_dir_17 + lbm_s_run_dir


    # 621 wrf_s
    wrf_s = Process()
    wrf_s_dir = '621.wrf_s/'
    wrf_s_run_dir = wrf_s_dir + refspeed_run_dir
    wrf_s.executable = bench_dir_17 + wrf_s_run_dir\
	 + 'wrf_s' + exe_suffix
    # no data
    wrf_s.cmd = [wrf_s.executable]
    wrf_s.output = 'wrf_s.out'
    wrf_s.cwd = bench_dir_17 + wrf_s_run_dir

    # 627 cam4_s
    cam4_s = Process()
    cam4_s_dir = '627.cam4_s/'
    cam4_s_run_dir = cam4_s_dir + refspeed_run_dir
    cam4_s.executable = bench_dir_17 + cam4_s_run_dir + 'cam4_s' + exe_suffix
    # no data
    cam4_s.cmd = [cam4_s.executable]
    cam4_s.output = 'cam4_s.out'
    cam4_s.cwd = bench_dir_17 + cam4_s_run_dir

    # 628 pop2_s
    pop2_s = Process()
    pop2_s_dir = '628.pop2_s/'
    pop2_s_run_dir = pop2_s_dir + refspeed_run_dir
    pop2_s.executable = bench_dir_17 + pop2_s_run_dir +\
	 'speed_pop2' + exe_suffix
    # no data
    pop2_s.cmd = [pop2_s.executable]
    pop2_s.output = 'pop2_s.out'
    pop2_s.cwd = bench_dir_17 + pop2_s_run_dir

    # 638 imagick_s
    imagick_s = Process()
    imagick_s_dir = '638.imagick_s/'
    imagick_s_run_dir = imagick_s_dir + refspeed_run_dir
    imagick_s.executable = bench_dir_17 + imagick_s_run_dir\
	 + 'imagick_s' + exe_suffix
    imagick_s_data = 'refspeed_input.tga'
    imagick_s.cmd = [imagick_s.executable] + ['-limit','disk','0',
		    imagick_s_data,'-resize','817%',
                    '-rotate','-2.76','-shave','540x375',
		    '-alpha','remove','-auto-level','-contrast-stretch',
                    '1x1%','-colorspace','Lab','-channel','R',
		    '-equalize','+channel','colorspace',
                    'sRGB','-define','histogram:unique-colors=false',
		    '-adaptive-blur','0x5','-despeckle',
                    '-auto-gamma','-adaptive-sharpen','55','-enhance',
		    '-brightness-contrast','10x10','-resize',
                    '30%','refspeed_output.tga']
    imagick_s.output = 'refspeed_convert.out'
    imagick_s.cwd = bench_dir_17 + imagick_s_run_dir

    # 644 nab_s
    nab_s = Process()
    nab_s_dir = '644.nab_s/'
    nab_s_run_dir = nab_s_dir + refspeed_run_dir
    nab_s.executable = bench_dir_17 + nab_s_run_dir + 'nab_s' + exe_suffix
    nab_s_data = '3j1n'
    nab_s.cmd = [nab_s.executable] + [nab_s_data, '20140317','220']
    nab_s.output = '3j1n.out'
    nab_s.cwd = bench_dir_17 + nab_s_run_dir

    # 649 fotonik3d_s
    fotonik3d_s = Process()
    fotonik3d_s_dir = '649.fotonik3d_s/'
    fotonik3d_s_run_dir = fotonik3d_s_dir + refspeed_run_dir
    fotonik3d_s.executable = bench_dir_17 + fotonik3d_s_run_dir + 'fotonik3d_s' + exe_suffix
    # no data
    fotonik3d_s.cmd = [fotonik3d_s.executable]
    fotonik3d_s.output = 'fotonik3d_s.log'
    fotonik3d_s.cwd = bench_dir_17 + fotonik3d_s_run_dir

    # 654 rom_s
    roms_s = Process()
    roms_s_dir = '654.roms_s/'
    roms_s_run_dir = roms_s_dir + refspeed_run_dir
    roms_s.executable = bench_dir_17 + roms_s_run_dir + 'sroms' + exe_suffix
    roms_s_data = 'ocean_benchmark3.in.x'
    roms_s.cmd = [roms_s.executable]
    roms_s.output = 'roms_s.out'
    roms_s.input = bench_dir_17 + roms_s_run_dir + roms_s_data
    roms_s.cwd = bench_dir_17 + roms_s_run_dir
    # 996 specrand_fs
    specrand_fs = Process()
    specrand_fs_dir = '996.specrand_fs/'
    specrand_fs_run_dir = specrand_fs_dir + refspeed_run_dir
    specrand_fs.executable = bench_dir_17 + specrand_fs_run_dir + 'specrand_fs' + exe_suffix
    # no data
    specrand_fs.cmd = [specrand_fs.executable] + ['1255432124','234923']
    specrand_fs.output = 'rand.234923.out'

    ## Integer Speed

    # 600 perlbench_s
    perlbench_s = Process()
    perlbench_s_dir = '600.perlbench_s/'
    perlbench_s_run_dir = perlbench_s_dir + refspeed_run_dir
    perlbench_s.executable = bench_dir_17 + perlbench_s_run_dir + 'perlbench_s' + exe_suffix
    perlbench_s_data = 'checkspam.pl'
    perlbench_s.cmd = [perlbench_s.executable] + ['-I./lib',perlbench_s_data,'2500','5','25','11','150',
                        '1','1','1','1']
    perlbench_s.output = 'checkspam.2500.5.25.11.150.1.1.1.1.out'
    perlbench_s.cwd = bench_dir_17 + perlbench_s_run_dir

    # 602 gcc_s
    gcc_s = Process()
    gcc_s_dir = '602.gcc_s/'
    gcc_s_run_dir = gcc_s_dir + refspeed_run_dir
    gcc_s.executable = bench_dir_17 + gcc_s_run_dir + 'sgcc' + exe_suffix
    gcc_s_data = 'gcc-pp.c'
    gcc_s.cmd = [gcc_s.executable] + [gcc_s_data,'-O5',
	'-finline-limit=24000','-fgcse','-fgcse-las',
	'-fgcse-lm','-fgcse-sm','-o',
	'gcc-pp.opts-O5_-finline-limit_24000_-fgcse_-fgcse-las_-fgcse-lm_-fgcse-sm.s']
    gcc_s.output = 'gcc-pp.opts-O5_-finline-limit_24000_-fgcse_-fgcse-las_-fgcse-lm_-fgcse-sm.out'
    gcc_s.cwd = bench_dir_17 + gcc_s_run_dir

    # 605 mcf_s
    mcf_s = Process()
    mcf_s_dir = '605.mcf_s/'
    mcf_s_run_dir = mcf_s_dir + refspeed_run_dir
    mcf_s.executable = bench_dir_17 + mcf_s_run_dir + 'mcf_s' + exe_suffix
    mcf_s_data = 'inp.in'
    mcf_s.cmd = [mcf_s.executable] + [mcf_s_data]
    mcf_s.output = 'inp.out'
    mcf_s.cwd = bench_dir_17 + mcf_s_run_dir

    # 620 omnetpp_s
    omnetpp_s = Process()
    omnetpp_s_dir = '620.omnetpp_s/'
    omnetpp_s_run_dir = omnetpp_s_dir + refspeed_run_dir
    omnetpp_s.executable = bench_dir_17 + omnetpp_s_run_dir + 'omnetpp_s' + exe_suffix
    # no data?
    omnetpp_s.cmd = [omnetpp_s.executable] + ['-c','General','-r','0']
    omnetpp_s.output = 'omnetpp.General-0.out'
    omnetpp_s.cwd = bench_dir_17 + omnetpp_s_run_dir

    # 623 xalancbmk_s
    xalancbmk_s = Process()
    xalancbmk_s_dir = '623.xalancbmk_s/'
    xalancbmk_s_run_dir = xalancbmk_s_dir + refspeed_run_dir
    xalancbmk_s.executable = bench_dir_17 + xalancbmk_s_run_dir + 'xalancbmk_s' + exe_suffix
    xalancbmk_s_data_1 = 't5.xml'
    xalancbmk_s_data_2 = 'xalanc.xsl'
    xalancbmk_s.cmd = [xalancbmk_s.executable] + ['-v',xalancbmk_s_data_1,xalancbmk_s_data_2]
    xalancbmk_s.output = 'ref-t5.out'
    xalancbmk_s.cwd = bench_dir_17 + xalancbmk_s_run_dir

    # 625 x264_s
    x264_s = Process()
    x264_s_dir = '625.x264_s/'
    x264_s_run_dir = x264_s_dir + refspeed_run_dir
    x264_s.executable = bench_dir_17 + x264_s_run_dir + 'x264_s' + exe_suffix
    # no data
    x264_s.cmd = [x264_s.executable] + ['--pass','1','--stats','x264_stats.log','--bitrate','1000',
                    '--frames','1000','-o','BuckBunny_New.264','BuckBunny.yuv','1280x720']
    x264_s.output = 'run_000-1000_x264_s_base.spectre_safebet-m64_x264_pass1.out'
    x264_s.cwd = bench_dir_17 + x264_s_run_dir

    # 631 deepsjeng_s
    deepsjeng_s = Process()
    deepsjeng_s_dir = '631.deepsjeng_s/'
    deepsjeng_s_run_dir = deepsjeng_s_dir + refspeed_run_dir
    deepsjeng_s.executable = bench_dir_17 +\
	 deepsjeng_s_run_dir + 'deepsjeng_s' + exe_suffix
    deepsjeng_s_data = 'ref.txt'
    deepsjeng_s.cmd = [deepsjeng_s.executable] + [deepsjeng_s_data]
    deepsjeng_s.output = 'ref.out'
    deepsjeng_s.cwd = bench_dir_17 + deepsjeng_s_run_dir

    # 641 leela_s
    leela_s = Process()
    leela_s_dir = '641.leela_s/'
    leela_s_run_dir = leela_s_dir + refspeed_run_dir
    leela_s.executable = bench_dir_17 + leela_s_run_dir\
	 + 'leela_s' + exe_suffix
    leela_s_data = 'ref.sgf'
    leela_s.cmd = [leela_s.executable] + [leela_s_data]
    leela_s.output = output_dir + 'ref.out'
    leela_s.cwd = bench_dir_17 + leela_s_run_dir

    # 648 exchange2_s
    exchange2_s = Process()
    exchange2_s_dir = '648.exchange2_s/'
    exchange2_s_run_dir = exchange2_s_dir + refspeed_run_dir
    exchange2_s.executable = bench_dir_17 + exchange2_s_run_dir +\
	 'exchange2_s' + exe_suffix
    # no data
    exchange2_s.cmd = [exchange2_s.executable] + ['6']
    exchange2_s.output = 'exchange2.txt'
    exchange2_s.cwd = bench_dir_17 + exchange2_s_run_dir

    # 657 xz_s
    xz_s = Process()
    xz_s_dir = '657.xz_s/'
    xz_s_run_dir = xz_s_dir + refspeed_run_dir
    xz_s.executable = bench_dir_17 + xz_s_run_dir + 'xz_s' + exe_suffix
    xz_s_data = 'cld.tar.xz'
    #xz_s_data = 'cpu2006docs.tar.xz'
    #xz_s.cmd = [xz_s.executable] + [xz_s_data,'6643',
    #    '1036078272','1111795472','4']
    xz_s.cmd = [xz_s.executable] + [xz_s_data, '1400', '19cf30ae51eddcbefda78dd06014b4b96281456e078ca7c13e1c0c9e6aaea8dff3efb4ad6b0456697718cede6bd5454852652806a657bb56e07d61128434b474', '536995164', '539938872', '8']
    xz_s.output = 'cpu2006docs.tar-6643-4.out'
    xz_s.cwd = bench_dir_17 + xz_s_run_dir

    # 998 specrand_is
    specrand_is = Process()
    specrand_is_dir = '998.specrand_is/'
    specrand_is_run_dir = specrand_is_dir + refspeed_run_dir
    specrand_is.executable = bench_dir_17 + specrand_is_run_dir + 'specrand_is' + exe_suffix
    # no data
    specrand_is.cmd = [specrand_is.executable] + ['1255432124','234923']
    specrand_is.output = 'rand.234923.out'


    ## Floating Point Rate

    # unused at the moment

    # bwaves_r
    bwaves_r = Process()
    bwaves_r_dir = '503.bwaves_r/'
    bwaves_r_run_dir = bwaves_r_dir + refrate_run_dir
    bwaves_r.executable = bench_dir_17 + bwaves_r_run_dir + 'bwaves_r'  + exe_suffix
    bwaves_r_data = 'bwaves_1.in'
    bwaves_r.cmd = [bwaves_r.executable] + [bwaves_r_data]
    bwaves_r.output = 'bwaves.out'

    # cactuBSSN_r
    cactuBSSN_r = Process()
    cactuBSSN_r_dir = '507.cactuBSSN_r'
    cactuBSSN_r_run_dir = cactuBSSN_r_dir + refrate_run_dir
    cactuBSSN_r.executable = bench_dir_17 + cactuBSSN_r_run_dir + 'cactuBSSN_r' + exe_suffix
    cactuBSSN_r_data = 'spec_ref.par'
    cactuBSSN_r.cmd = [cactuBSSN_r.executable] + [cactuBSSN_r_data]
    cactuBSSN_r.output = 'cactuBSSN.out'

    # lbm_r
    lbm_r = Process()
    lbm_r_dir = '519.lbm_r/'
    # lbm_run_dir = 'run/run_base_test_spectre_safebet-m64.0000/'
    lbm_r_run_dir = lbm_r_dir + refrate_run_dir
    lbm_r.executable = bench_dir_17 + lbm_r_run_dir + 'lbm_r_base.spectre_safebet-m64'
    lbm_r_data = '100_100_130_cf_a.of'
    lbm_r.cmd = [lbm_r.executable] + ['20','reference.dat','0','1',lbm_r_data]
    lbm_r.output = 'lbm.out'


    # for the legacy stuff (probably unnecessary)
    if buildEnv['TARGET_ISA'] == 'arm':
        benchtype = "-armcross"
    elif buildEnv['TARGET_ISA'] == 'x86':
        benchtype = '-m64-gcc43-nn'
    else:
        sys.exit("Unsupported ISA")

    #400.perlbench
    perlbench = Process()
    perlbench_dir = '400.perlbench/'
    perlbench.executable =  exe_dir_06+perlbench_dir+\
    'exe/perlbench' + exe_suffix
    perlbench.cmd = [perlbench.executable] +\
        ['-I./lib', 'checkspam.pl', '2500', '5', '25',\
        '11', '150', '1', '1', '1', '1' ]
    perlbench.cwd = bench_dir_06+perlbench_dir+'run/'
    perlbench.output = 'attrs.out'

    #401.bzip2
    bzip2 = Process()
    bzip2_dir = '401.bzip2/'
    bzip2.executable =  exe_dir_06+bzip2_dir+\
        'exe/bzip2' 
    data= bench_dir_06+bzip2_dir+'data/ref/input/input.source'
    bzip2.cmd = [bzip2.executable] + [data, '1']
    bzip2.output = 'input.source.out'

    #403.gcc
    gcc = Process()
    gcc_dir = '403.gcc/'
    gcc.executable =  exe_dir_06+gcc_dir+\
        'exe/gcc' 
    data= bench_dir_06+gcc_dir+'/data/ref/input/166.i'
    output=output_dir+'166.s'
    gcc.cmd = [gcc.executable] + [data]+['-o',output] + ['-quiet'] \
    + ['-funroll-loops'] + ['-fforce-mem'] + ['-fcse-follow-jumps'] \
    + ['-fcse-skip-blocks'] + ['-fexpensive-optimizations'] \
    + ['-fstrength-reduce'] + ['-fpeephole']  + ['-fschedule-insns'] \
    + ['-finline-functions'] + ['-fschedule-insns2']

    #410.bwaves
    bwaves = Process()
    bwaves_dir= bench_dir_06+'410.bwaves'
    bwaves.executable =  exe_dir_06+'410.bwaves/'+'exe/bwaves' 
    bwaves.cwd = bwaves_dir+'run/'
    bwaves.cmd = [bwaves.executable]


    #429.mcf
    mcf = Process()
    mcf_dir = '429.mcf/'
    mcf.executable = exe_dir_06+mcf_dir+\
        'exe/mcf' + exe_suffix
    data= bench_dir_06+mcf_dir+'/data/ref/input/inp.in'
    mcf.cmd = [mcf.executable] + ['inp.in']
    mcf.cwd = bench_dir_06+mcf_dir+'run/'
    mcf.output = 'inp.out'


    #433.milc
    milc=Process()
    milc_dir='433.milc/'
    milc.executable = exe_dir_06+milc_dir+\
        'exe/milc' + exe_suffix
    stdin= bench_dir_06+milc_dir+'/data/ref/input/su3imp.in'
    milc.cmd = [milc.executable]
    milc.input=stdin
    milc.output='su3imp.out'

    #436.cactusADM
    cactusADM = Process()
    cactusADM_dir = '436.cactusADM/'
    cactusADM.executable =  exe_dir_06+cactusADM_dir+\
      'exe/cactusADM' + exe_suffix
    data= bench_dir_06+cactusADM_dir+'/data/ref/input/benchADM.par'
    cactusADM.cmd = [cactusADM.executable] + ['benchADM.par']
    cactusADM.cwd = bench_dir_06+cactusADM_dir + 'run'
    cactusADM.output = 'benchADM.out'

    #437.leslie3d
    leslie3d=Process()
    leslie3d_dir= '437.leslie3d/'
    leslie3d.executable = exe_dir_06+leslie3d_dir+\
        'exe/leslie3d' + exe_suffix
    stdin= bench_dir_06+leslie3d_dir+'/data/ref/input/leslie3d.in'
    leslie3d.cmd = [leslie3d.executable]
    leslie3d.input=stdin
    leslie3d.output='leslie3d.stdout'


    #444.namd
    namd = Process()
    namd_dir='444.namd/'
    namd.executable =  exe_dir_06+namd_dir+\
        'exe/namd' + exe_suffix
    input= bench_dir_06+namd_dir+'/data/all/input/namd.input'
    namd.cmd = [namd.executable] + ['--input',input,'--iterations','1',\
        '--output','namd.out']
    namd.output='namd.stdout'


    #453.povray
    povray=Process()
    povray_dir = '453.povray/'
    povray.executable = exe_dir_06+povray_dir+\
        'exe/povray' + exe_suffix
    data= bench_dir_06+povray_dir+'/data/ref/input/SPEC-benchmark-ref.ini'
    povray.cmd = [povray.executable]+[data]
    povray.output = 'SPEC-benchmark-ref.stdout'



    #456.hmmer
    hmmer=Process()
    hmmr_dir = '456.hmmer/'
    hmmer.executable = exe_dir_06+hmmr_dir+\
        'exe/hmmer' + exe_suffix
    data= bench_dir_06+hmmr_dir+'/data/ref/input/nph3.hmm'
    hmmer.cmd = [hmmer.executable]+['--fixed', '0', '--mean', '325',\
        '--num', '5000', '--sd', '200', '--seed', '0', data]
    hmmer.output = 'bombesin.out'


    #458.sjeng
    sjeng=Process()
    sjeng_dir = '458.sjeng/'
    sjeng.executable =  exe_dir_06+sjeng_dir+\
        'exe/sjeng' + exe_suffix
    data= bench_dir_06+sjeng_dir+'/data/ref/input/ref.txt'
    sjeng.cmd = [sjeng.executable]+[data]
    sjeng.output = 'ref.out'


    #465.tonto
    tonto=Process()
    tonto_dir = '465.tonto/'
    tonto.executable = exe_dir_06+tonto_dir+\
        'exe/tonto' + exe_suffix
    data= bench_dir_06+tonto_dir+'/data/ref/input/foreman_ref_encoder_baseline.cfg'
    tonto.cmd = [tonto.executable]
    tonto.cwd = bench_dir_06+tonto_dir+'run'
    tonto.output = 'tonto.out'

    #470.lbm
    lbm=Process()
    lbm_dir='470.lbm/'
    lbm.executable = exe_dir_06+lbm_dir+\
        'exe/lbm' + exe_suffix
    data= bench_dir_06+lbm_dir+'/data/ref/input/100_100_130_ldc.of'
    lbm.cmd = [lbm.executable]+['20', 'reference.dat', '0', '1' ,data]
    lbm.output = 'lbm.out'


    #471.omnetpp
    omnetpp=Process()
    omnetpp_dir = '471.omnetpp/'
    omnetpp.executable =  exe_dir_06+omnetpp_dir+\
        'exe/omnetpp' + exe_suffix
    data= bench_dir_06+omnetpp_dir+'/data/ref/input/omnetpp.ini'
    omnetpp.cmd = [omnetpp.executable]+[data]
    omnetpp.output = 'omnetpp.log'

    #473.astar
    astar=Process()
    astar_dir='473.astar/'
    astar.executable = exe_dir_06+astar_dir+\
        'exe/astar' + exe_suffix
    data= bench_dir_06+astar_dir+'/data/test/input/lake.cfg'
    astar.cmd = [astar.executable]+[data]
    astar.cwd = bench_dir_06+astar_dir+'/data/test/input/'
    astar.output = 'lake.out'

    #481.wrf
    wrf=Process()
    wrf_dir = '481.wrf/'
    wrf.executable = exe_dir_06+wrf_dir+\
        'exe/wrf' + exe_suffix
    data = bench_dir_06+wrf_dir+'/data/ref/input/namelist.input'
    wrf.cmd = [wrf.executable]+[data]
    wrf.output = 'rsl.out.0000'

    #482.sphinx
    sphinx3=Process()
    sphinx3_dir = '482.sphinx3/'
    sphinx3.executable =  exe_dir_06+sphinx3_dir+\
       'exe/sphinx_livepretend' + exe_suffix
    sphinx3.cmd = [sphinx3.executable]+['ctlfile', '.', 'args.an4']
    sphinx3.cwd = bench_dir_06+sphinx3_dir + 'run/'
    sphinx3.output = 'an4.out'

    #483.xalancbmk
    xalancbmk=Process()
    xalanch_dir = '483.xalancbmk/'
    xalancbmk.executable =  exe_dir_06+xalanch_dir+\
        'exe/Xalan' + exe_suffix
    data = bench_dir_06 + xalanch_dir + '/data/ref/input/'
    xalancbmk.cmd = [xalancbmk.executable]+['-v','t5.xml','xalanc.xsl']
    xalancbmk.cwd = bench_dir_06+xalanch_dir+'run'
    xalancbmk.output = 'ref.out'

    # ## TEST PROCESS
    # test_proc = Process()
    # test_proc.executable = '/home/min/a/nelso345/spectre-research/test.elf'
    # test_proc.cmd = [test_proc.executable]
    # test_proc.output = '/dev/null'
    # test_proc.input = '/dev/null'

    ### both


    if options.benchmark == 'perlbench_s':
       process = perlbench_s
    elif options.benchmark == 'gcc_s':
       process = gcc_s
    elif options.benchmark == 'bwaves_s':
       process = bwaves_s
    elif options.benchmark == 'mcf_s':
       process = mcf_s
    elif options.benchmark == 'cactuBSSN_s':
       process = cactuBSSN_s
    elif options.benchmark == 'deepsjeng_s':
       process = deepsjeng_s
    elif options.benchmark == 'lbm_s':
       process = lbm_s
    elif options.benchmark == 'omnetpp_s':
       process = omnetpp_s
    elif options.benchmark == 'wrf_s':
       process = wrf_s
    elif options.benchmark == 'xalancbmk_s':
       process = xalancbmk_s
    elif options.benchmark == 'specrand_is':
       process = specrand_is
    elif options.benchmark == 'specrand_fs':
       process = specrand_fs
    elif options.benchmark == 'cam4_s':
        process = cam4_s
    elif options.benchmark == 'pop2_s':
        process = pop2_s
    elif options.benchmark == 'imagick_s':
        process = imagick_s
    elif options.benchmark == 'nab_s':
        process = nab_s
    elif options.benchmark == 'fotonik3d_s':
        process = fotonik3d_s
    elif options.benchmark == 'roms_s':
        process = roms_s
    elif options.benchmark == 'x264_s':
        process = x264_s
    elif options.benchmark == 'leela_s':
        process = leela_s
    elif options.benchmark == 'exchange2_s':
        process = exchange2_s
    elif options.benchmark == 'xz_s':
        process = xz_s
    elif options.benchmark == 'perlbench':
       process = perlbench
    elif options.benchmark == 'bzip2':
       process = bzip2
    elif options.benchmark == 'gcc':
       process = gcc
    elif options.benchmark == 'bwaves':
       process = bwaves
    elif options.benchmark == 'gamess':
       process = gamess
    elif options.benchmark == 'mcf':
       process = mcf
    elif options.benchmark == 'milc':
       process = milc
    elif options.benchmark == 'zeusmp':
       process = zeusmp
    elif options.benchmark == 'gromacs':
       process = gromacs
       shutil.copy(os.path.join(process.cwd,"gromacs.tpr"),os.getcwd())
    elif options.benchmark == 'cactusADM':
       process = cactusADM
    elif options.benchmark == 'leslie3d':
       process = leslie3d
    elif options.benchmark == 'namd':
       process = namd
    elif options.benchmark == 'gobmk':
       process = gobmk;
    elif options.benchmark == 'dealII':
       process = dealII
    elif options.benchmark == 'soplex':
       process = soplex
    elif options.benchmark == 'povray':
       process = povray
    elif options.benchmark == 'calculix':
       process = calculix
    elif options.benchmark == 'hmmer':
       process = hmmer
    elif options.benchmark == 'sjeng':
       process = sjeng
    elif options.benchmark == 'GemsFDTD':
       process = GemsFDTD
    elif options.benchmark == 'libquantum':
       process = libquantum
    elif options.benchmark == 'h264ref':
       process = h264ref
    elif options.benchmark == 'tonto':
       process = tonto
    elif options.benchmark == 'lbm':
       process = lbm
    elif options.benchmark == 'omnetpp':
       process = omnetpp
    elif options.benchmark == 'astar':
       process = astar
    elif options.benchmark == 'wrf':
       process = wrf
    elif options.benchmark == 'sphinx3':
       process = sphinx3
    elif options.benchmark == 'xalancbmk':
       process = xalancbmk
    elif options.benchmark == 'specrand_i':
       process = specrand_i
    elif options.benchmark == 'specrand_f':
       process = specrand_f
    # elif options.benchmark == 'test':
    #     process = test_proc
    return process
