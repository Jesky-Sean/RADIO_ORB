#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: AllSeeingEye_Of_Attacks
# Author: seanMJ
# Description: Listens to all network aspects i can find and utilize.
# GNU Radio version: 3.10.12.0

from gnuradio import analog
import math
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr, blocks
import pmt
from gnuradio.filter import pfb
import threading
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation




class FmModListen(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "AllSeeingEye_Of_Attacks", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.vec_sz_1 = vec_sz_1 = 1
        self.vec_sz = vec_sz = 1
        self.taps_C_0_0 = taps_C_0_0 = 3
        self.taps_C = taps_C = 4
        self.stopBand_C = stopBand_C = 100
        self.samplesToSymbols = samplesToSymbols = 8
        self.samp_rate = samp_rate = 48000
        self.gain_C = gain_C = 1
        self.fileName_WAV_PSKMOD_C = fileName_WAV_PSKMOD_C = "/home/sean/audioSamples/DAT/aug-2026/FirstWAVRun_PSKMOD"
        self.fileName_WAV_B = fileName_WAV_B = "/home/sean/audioSamples/DAT/aug-2026/FirstWAVRun_bandpassFilter"
        self.fileName_WAV_AM_A = fileName_WAV_AM_A = "/home/sean/audioSamples/DAT/aug-2026/FirstWAVRun_AMMOD.wav"
        self.fileName_METADAT_AM_A = fileName_METADAT_AM_A = "/home/sean/audioSamples/DAT/aug-2026/FirstRun_Meta-FirstWAVRun_AMMOD"
        self.fileName_DAT_PSKMOD_C = fileName_DAT_PSKMOD_C = "/home/sean/audioSamples/DAT/aug-2026/FirstRun_PSKMOD"
        self.fileName_DAT_B_BNDPASS = fileName_DAT_B_BNDPASS = "/home/sean/audioSamples/DAT/aug-2026/FirstRun_bandpassFilter"
        self.decimations = decimations = 1
        self.channelRate_1 = channelRate_1 = 100000
        self.channelRate = channelRate = 100000
        self.audioStop_C = audioStop_C = 4000
        self.audioStop = audioStop = 4700
        self.audioPass_C = audioPass_C = 300
        self.audioPass = audioPass = 200
        self.audioDecimations = audioDecimations = 3
        self.TransitionWidth = TransitionWidth = 1000
        self.RMS_ = RMS_ = 00.5
        self.QuatGain_C = QuatGain_C = 3
        self.PolyphsdrDecimations_C = PolyphsdrDecimations_C = 2
        self.BitsScale_C = BitsScale_C = 6
        self.BandPass_lw_B = BandPass_lw_B = 1
        self.BandPass_hg_B = BandPass_hg_B = 8000

        ##################################################
        # Blocks
        ##################################################

        self.pfb_decimator_ccf_1 = pfb.decimator_ccf(
            PolyphsdrDecimations_C,
            [taps_C],
            0,
            stopBand_C,
            True,
            True)
        self.pfb_decimator_ccf_1.declare_sample_delay(0)
        self.filenameForData_0 = blocks.wavfile_sink(
            fileName_WAV_AM_A,
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_FLOAT,
            False
            )
        self.filenameForData = blocks.wavfile_sink(
            fileName_WAV_B,
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_FLOAT,
            False
            )
        self.digital_psk_demod_0 = digital.psk.psk_demod(
            constellation_points=8,
            differential=True,
            samples_per_symbol=samplesToSymbols,
            excess_bw=.2,
            phase_bw=(3.28/100.0),
            timing_bw=(3.28/100.0),
            mod_code="gray",
            verbose=True,
            log=True,
            improved_fll=True)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff((vec_sz+4096), True)
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink(
            fileName_WAV_PSKMOD_C,
            1,
            samp_rate,
            blocks.FORMAT_WAV,
            blocks.FORMAT_FLOAT,
            False
            )
        self.blocks_throttle2_0_1 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*vec_sz, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_tag_gate_0_1 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0_1.set_single_key("")
        self.blocks_tag_gate_0_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0_0.set_single_key("")
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_tag_gate_0.set_single_key("")
        self.blocks_rms_xx_0 = blocks.rms_ff(.001)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(2)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar(1, 1, 0)
        self.blocks_float_to_complex_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(vec_sz)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0_0_0 = blocks.file_sink(gr.sizeof_float*1, fileName_DAT_B_BNDPASS, True)
        self.blocks_file_sink_0_0_0.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, fileName_DAT_PSKMOD_C, True)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*1, fileName_METADAT_AM_A, samp_rate, 1, blocks.GR_FILE_FLOAT, True, 1000000, pmt.make_dict(), False)
        self.blocks_file_meta_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, BitsScale_C)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                BandPass_lw_B,
                BandPass_hg_B,
                TransitionWidth,
                window.WIN_HAMMING,
                6.76))
        self.audio_source_0 = audio.source(48000, 'hw:H6,0', True)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(QuatGain_C)
        self.analog_fm_preemph_1_0 = analog.fm_preemph(fs=samp_rate, tau=(75e-6), fh=(-1.0))
        self.analog_fm_preemph_1 = analog.fm_preemph(fs=samp_rate, tau=(75e-6), fh=(-.001))
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=channelRate,
        	audio_decim=decimations,
        	audio_pass=audioPass,
        	audio_stop=audioStop,
        )
        self.RMS_values = blocks.rms_ff(RMS_)
        self.BandpassRMS = blocks.rms_ff(RMS_)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.BandpassRMS, 0), (self.blocks_tag_gate_0_1, 0))
        self.connect((self.RMS_values, 0), (self.blocks_tag_gate_0_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.analog_fm_preemph_1, 0), (self.blocks_float_to_complex_1, 0))
        self.connect((self.analog_fm_preemph_1_0, 0), (self.blocks_float_to_complex_1_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.audio_source_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_throttle2_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.blocks_throttle2_0_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_file_meta_sink_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.pfb_decimator_ccf_1, 0))
        self.connect((self.blocks_float_to_complex_1, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.RMS_values, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.BandpassRMS, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.filenameForData_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.blocks_file_sink_0_0_0, 0))
        self.connect((self.blocks_tag_gate_0_0, 0), (self.filenameForData, 0))
        self.connect((self.blocks_tag_gate_0_1, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_tag_gate_0_1, 0), (self.blocks_wavfile_sink_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle2_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_throttle2_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.analog_fm_preemph_1, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.analog_fm_preemph_1_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.digital_psk_demod_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.pfb_decimator_ccf_1, 0), (self.digital_psk_demod_0, 0))


    def get_vec_sz_1(self):
        return self.vec_sz_1

    def set_vec_sz_1(self, vec_sz_1):
        self.vec_sz_1 = vec_sz_1

    def get_vec_sz(self):
        return self.vec_sz

    def set_vec_sz(self, vec_sz):
        self.vec_sz = vec_sz

    def get_taps_C_0_0(self):
        return self.taps_C_0_0

    def set_taps_C_0_0(self, taps_C_0_0):
        self.taps_C_0_0 = taps_C_0_0

    def get_taps_C(self):
        return self.taps_C

    def set_taps_C(self, taps_C):
        self.taps_C = taps_C
        self.pfb_decimator_ccf_1.set_taps([self.taps_C])

    def get_stopBand_C(self):
        return self.stopBand_C

    def set_stopBand_C(self, stopBand_C):
        self.stopBand_C = stopBand_C

    def get_samplesToSymbols(self):
        return self.samplesToSymbols

    def set_samplesToSymbols(self, samplesToSymbols):
        self.samplesToSymbols = samplesToSymbols

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.BandPass_lw_B, self.BandPass_hg_B, self.TransitionWidth, window.WIN_HAMMING, 6.76))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle2_0_1.set_sample_rate(self.samp_rate)

    def get_gain_C(self):
        return self.gain_C

    def set_gain_C(self, gain_C):
        self.gain_C = gain_C

    def get_fileName_WAV_PSKMOD_C(self):
        return self.fileName_WAV_PSKMOD_C

    def set_fileName_WAV_PSKMOD_C(self, fileName_WAV_PSKMOD_C):
        self.fileName_WAV_PSKMOD_C = fileName_WAV_PSKMOD_C
        self.blocks_wavfile_sink_0_0.open(self.fileName_WAV_PSKMOD_C)

    def get_fileName_WAV_B(self):
        return self.fileName_WAV_B

    def set_fileName_WAV_B(self, fileName_WAV_B):
        self.fileName_WAV_B = fileName_WAV_B
        self.filenameForData.open(self.fileName_WAV_B)

    def get_fileName_WAV_AM_A(self):
        return self.fileName_WAV_AM_A

    def set_fileName_WAV_AM_A(self, fileName_WAV_AM_A):
        self.fileName_WAV_AM_A = fileName_WAV_AM_A
        self.filenameForData_0.open(self.fileName_WAV_AM_A)

    def get_fileName_METADAT_AM_A(self):
        return self.fileName_METADAT_AM_A

    def set_fileName_METADAT_AM_A(self, fileName_METADAT_AM_A):
        self.fileName_METADAT_AM_A = fileName_METADAT_AM_A
        self.blocks_file_meta_sink_0.open(self.fileName_METADAT_AM_A)

    def get_fileName_DAT_PSKMOD_C(self):
        return self.fileName_DAT_PSKMOD_C

    def set_fileName_DAT_PSKMOD_C(self, fileName_DAT_PSKMOD_C):
        self.fileName_DAT_PSKMOD_C = fileName_DAT_PSKMOD_C
        self.blocks_file_sink_0_0.open(self.fileName_DAT_PSKMOD_C)

    def get_fileName_DAT_B_BNDPASS(self):
        return self.fileName_DAT_B_BNDPASS

    def set_fileName_DAT_B_BNDPASS(self, fileName_DAT_B_BNDPASS):
        self.fileName_DAT_B_BNDPASS = fileName_DAT_B_BNDPASS
        self.blocks_file_sink_0_0_0.open(self.fileName_DAT_B_BNDPASS)

    def get_decimations(self):
        return self.decimations

    def set_decimations(self, decimations):
        self.decimations = decimations

    def get_channelRate_1(self):
        return self.channelRate_1

    def set_channelRate_1(self, channelRate_1):
        self.channelRate_1 = channelRate_1

    def get_channelRate(self):
        return self.channelRate

    def set_channelRate(self, channelRate):
        self.channelRate = channelRate

    def get_audioStop_C(self):
        return self.audioStop_C

    def set_audioStop_C(self, audioStop_C):
        self.audioStop_C = audioStop_C

    def get_audioStop(self):
        return self.audioStop

    def set_audioStop(self, audioStop):
        self.audioStop = audioStop

    def get_audioPass_C(self):
        return self.audioPass_C

    def set_audioPass_C(self, audioPass_C):
        self.audioPass_C = audioPass_C

    def get_audioPass(self):
        return self.audioPass

    def set_audioPass(self, audioPass):
        self.audioPass = audioPass

    def get_audioDecimations(self):
        return self.audioDecimations

    def set_audioDecimations(self, audioDecimations):
        self.audioDecimations = audioDecimations

    def get_TransitionWidth(self):
        return self.TransitionWidth

    def set_TransitionWidth(self, TransitionWidth):
        self.TransitionWidth = TransitionWidth
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.BandPass_lw_B, self.BandPass_hg_B, self.TransitionWidth, window.WIN_HAMMING, 6.76))

    def get_RMS_(self):
        return self.RMS_

    def set_RMS_(self, RMS_):
        self.RMS_ = RMS_
        self.BandpassRMS.set_alpha(self.RMS_)
        self.RMS_values.set_alpha(self.RMS_)

    def get_QuatGain_C(self):
        return self.QuatGain_C

    def set_QuatGain_C(self, QuatGain_C):
        self.QuatGain_C = QuatGain_C
        self.analog_quadrature_demod_cf_0.set_gain(self.QuatGain_C)

    def get_PolyphsdrDecimations_C(self):
        return self.PolyphsdrDecimations_C

    def set_PolyphsdrDecimations_C(self, PolyphsdrDecimations_C):
        self.PolyphsdrDecimations_C = PolyphsdrDecimations_C

    def get_BitsScale_C(self):
        return self.BitsScale_C

    def set_BitsScale_C(self, BitsScale_C):
        self.BitsScale_C = BitsScale_C
        self.blocks_char_to_float_0_0.set_scale(self.BitsScale_C)

    def get_BandPass_lw_B(self):
        return self.BandPass_lw_B

    def set_BandPass_lw_B(self, BandPass_lw_B):
        self.BandPass_lw_B = BandPass_lw_B
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.BandPass_lw_B, self.BandPass_hg_B, self.TransitionWidth, window.WIN_HAMMING, 6.76))

    def get_BandPass_hg_B(self):
        return self.BandPass_hg_B

    def set_BandPass_hg_B(self, BandPass_hg_B):
        self.BandPass_hg_B = BandPass_hg_B
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, self.BandPass_lw_B, self.BandPass_hg_B, self.TransitionWidth, window.WIN_HAMMING, 6.76))




def main(top_block_cls=FmModListen, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        gr.logger("realtime").warn("Error: failed to enable real-time scheduling.")
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    main()
