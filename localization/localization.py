import os
from typing import Union

def L(s : Union[str, None]) -> Union[str, None]:
    return Localization.localize(s)

class Localization:
    lang = os.environ.get('__APP_LANGUAGE', 'en-US')
    allowed_langs = ['en-US', 'ru-RU', 'zh-CN', 'es-ES', 'it-IT', 'ja-JP', 'de-DE']

    @staticmethod
    def set_language(lang : str = None):
        if lang not in Localization.allowed_langs:
            raise Exception(f'{lang} not in allowed languages: {Localization.allowed_langs}')
        Localization.lang = lang
        os.environ['__APP_LANGUAGE'] = lang

    @staticmethod
    def localize(s : Union[str, None]) -> Union[str, None]:
        if s is None:
            return None

        if len(s) > 0 and s[0] == '@':
            x = Localization._id_to_string_dict.get(s[1:], None)
            if x is not None:
                return x[Localization.lang]
            else:
                print(f'Localization for {s} not found.')
        return s

    _id_to_string_dict = \
        {
            'misc.auto': {
                'en-US': 'Otomatis'
            },
            'misc.menu_select': {
                'en-US': '--Pilih--'
            },
            'common.device': {
                'en-US': 'Perangkat'
            },
            'common.help.device': {
                'en-US': 'Sesuaikan kombinasi perangkat modul untuk mencapai fps lebih tinggi atau penggunaan CPU lebih rendah.'
            },
            'QBackendPanel.start': {
                'en-US': 'Mulai'
            },
            'QBackendPanel.stop': {
                'en-US': 'Berhenti'
            },
            'QBackendPanel.reset_settings': {
                'en-US': 'Atur Ulang Pengaturan'
            },
            'QBackendPanel.FPS': {
                'en-US': 'FPS'
            },
            'QDFLAppWindow.file': {
                'en-US': 'Berkas'
            },
            'QDFLAppWindow.language': {
                'en-US': 'Bahasa'
            },
            'QDFLAppWindow.reset_modules_settings': {
                'en-US': 'Atur Ulang Pengaturan Modul'
            },
            'QDFLAppWindow.reinitialize': {
                'en-US': 'Inisialisasi Ulang'
            },
            'QDFLAppWindow.quit': {
                'en-US': 'Keluar'
            },
            'QDFLAppWindow.help': {
                'en-US': 'Bantuan'
            },
            'QDFLAppWindow.visit_github_page': {
                'en-US': 'Kunjungi Halaman GitHub'
            },
            'QDFLAppWindow.process_priority': {
                'en-US': 'Prioritas Proses'
            },
            'QDFLAppWindow.process_priority.lowest': {
                'en-US': 'Terendah'
            },
            'QDFLAppWindow.process_priority.normal': {
                'en-US': 'Normal'
            },
            'QFileSource.module_title': {
                'en-US': 'Sumber Berkas'
            },
            'QFileSource.target_width': {
                'en-US': 'Lebar Target'
            },
            'QFileSource.help.target_width': {
                'en-US': 'Ubah ukuran bingkai ke lebar yang diinginkan.'
            },
            'QFileSource.fps': {
                'en-US': 'FPS'
            },
            'QFileSource.help.fps': {
                'en-US': 'Atur bingkai per detik yang diinginkan.'
            },
            'QFileSource.is_realtime': {
                'en-US': 'Waktu Nyata'
            },
            'QFileSource.help.is_realtime': {
                'en-US': 'Apakah akan diputar dengan FPS waktu nyata atau secepat mungkin.'
            },
            'QFileSource.is_autorewind': {
                'en-US': 'Putar Ulang Otomatis'
            },
            'QCameraSource.module_title': {
                'en-US': 'Sumber Kamera'
            },
            'QCameraSource.device_index': {
                'en-US': 'Indeks Perangkat'
            },
            'QCameraSource.driver': {
                'en-US': 'Driver'
            },
            'QCameraSource.help.driver': {
                'en-US': 'Driver OS untuk mengoperasikan kamera.\nBeberapa driver dapat mendukung resolusi lebih tinggi, tetapi tidak mendukung pengaturan vendor.'
            },
            'QCameraSource.resolution': {
                'en-US': 'Resolusi'
            },
            'QCameraSource.help.resolution': {
                'en-US': 'Resolusi keluaran perangkat kamera.'
            },
            'QCameraSource.fps': {
                'en-US': 'FPS'
            },
            'QCameraSource.help.fps': {
                'en-US': 'Bingkai per detik keluaran perangkat kamera.'
            },
            'QCameraSource.rotation': {
                'en-US': 'Rotasi'
            },
            'QCameraSource.flip_horizontal': {
                'en-US': 'Balik Horizontal'
            },
            'QCameraSource.camera_settings': {
                'en-US': 'Pengaturan Kamera'
            },
            'QCameraSource.open_settings': {
                'en-US': 'Buka'
            },
            'QCameraSource.load_settings': {
                'en-US': 'Muat'
            },
            'QCameraSource.save_settings': {
                'en-US': 'Simpan'
            },
            'QFaceDetector.module_title': {
                'en-US': 'Detektor Wajah'
            },
            'QFaceDetector.detector_type': {
                'en-US': 'Detektor'
            },
            'QFaceDetector.help.detector_type': {
                'en-US': 'Jenis detektor bekerja secara berbeda.'
            },
            'QFaceDetector.window_size': {
                'en-US': 'Ukuran Jendela'
            },
            'QFaceDetector.help.window_size': {
                'en-US': 'Ukuran jendela yang lebih kecil lebih cepat, tetapi kurang akurat.'
            },
            'QFaceDetector.threshold': {
                'en-US': 'Ambang Batas'
            },
            'QFaceDetector.help.threshold': {
                'en-US': 'Nilai yang lebih rendah akan mendeteksi lebih banyak wajah palsu.'
            },
            'QFaceDetector.max_faces': {
                'en-US': 'Maksimum Wajah'
            },
            'QFaceDetector.help.max_faces': {
                'en-US': 'Jumlah maksimum wajah yang akan dideteksi.'
            },
            'QFaceDetector.sort_by': {
                'en-US': 'Urutkan Berdasarkan'
            },
            'QFaceDetector.help.sort_by': {
                'en-US': 'Urutkan wajah berdasarkan metode. Misalnya, untuk "KANAN KE KIRI", ID Wajah 0 akan berada di bagian paling kanan layar.'
            },
            'QFaceDetector.temporal_smoothing': {
                'en-US': 'Penghalusan Temporal'
            },
            'QFaceDetector.help.temporal_smoothing': {
                'en-US': 'Menstabilkan persegi panjang wajah dengan merata-ratakan bingkai.\nBagus untuk digunakan pada adegan statis atau dengan webcam.'
            },
            'QFaceDetector.detected_faces': {
                'en-US': 'Wajah yang Terdeteksi'
            },
            'QFaceAligner.module_title': {
                'en-US': 'Penyejajah Wajah'
            },
            'QFaceAligner.align_mode': {
                'en-US': 'Mode Penyejajaran'
            },
            'QFaceAligner.help.align_mode': {
                'en-US': 'Dari persegi panjang bagus untuk Animator Wajah. Dari titik bagus untuk penukar wajah.'
            },
            'QFaceAligner.face_coverage': {
                'en-US': 'Cakupan Wajah'
            },
            'QFaceAligner.help.face_coverage': {
                'en-US': 'Area keluaran wajah yang disejajarkan.\nSesuaikan sesuai keinginan.'
            },
            'QFaceAligner.resolution': {
                'en-US': 'Resolusi'
            },
            'QFaceAligner.help.resolution': {
                'en-US': 'Resolusi wajah yang disejajarkan.\nHarus sesuai dengan resolusi model.'
            },
            'QFaceAligner.exclude_moving_parts': {
                'en-US': 'Kecualikan Bagian Bergerak'
            },
            'QFaceAligner.help.exclude_moving_parts': {
                'en-US': 'Tingkatkan stabilisasi dengan mengecualikan landmark dari bagian wajah yang bergerak, seperti mulut dan lainnya.'
            },
            'QFaceAligner.head_mode': {
                'en-US': 'Mode Kepala'
            },
            'QFaceAligner.help.head_mode': {
                'en-US': 'Mode Kepala. Digunakan dengan model Kepala.'
            },
            'QFaceAligner.freeze_z_rotation': {
                'en-US': 'Bekukan Rotasi Z'
            },
            'QFaceAligner.x_offset': {
                'en-US': 'Offset X'
            },
            'QFaceAligner.y_offset': {
                'en-US': 'Offset Y'
            },
            'QFaceMarker.module_title': {
                'en-US': 'Penanda Wajah'
            },
            'QFaceMarker.marker_type': {
                'en-US': 'Penanda'
            },
            'QFaceMarker.help.marker_type': {
                'en-US': 'Jenis penanda wajah.'
            },
            'QFaceMarker.marker_coverage': {
                'en-US': 'Cakupan Penanda'
            },
            'QFaceMarker.help.marker_coverage': {
                'en-US': 'Mengontrol ukuran persegi panjang wajah yang terdeteksi untuk dimasukkan ke Penanda Wajah.\nTitik wajah hijau harus benar-benar sesuai dengan wajah.\nLihat jendela "Wajah yang Disejajarkan" dan sesuaikan sesuai keinginan.'
            },
            'QFaceMarker.temporal_smoothing': {
                'en-US': 'Penghalusan Temporal'
            },
            'QFaceMarker.help.temporal_smoothing': {
                'en-US': 'Menstabilkan landmark wajah dengan merata-ratakan bingkai.\nBagus untuk digunakan pada adegan statis atau dengan webcam.'
            },
            'QFaceAnimator.module_title': {
                'en-US': 'Animator Wajah'
            },
            'QFaceAnimator.animatable': {
                'en-US': 'Dapat Dianimasikan'
            },
            'QFaceAnimator.animator_face_id': {
                'en-US': 'ID Wajah Animator'
            },
            'QFaceAnimator.relative_power': {
                'en-US': 'Kekuatan Relatif'
            },
            'QFaceAnimator.reset_reference_pose': {
                'en-US': 'Atur Ulang Posisi Referensi'
            },
            'QFaceSwapper.module_title': {
                'en-US': 'Penukar Wajah'
            },
            'QFaceSwapper.model': {
                'en-US': 'Model'
            },
            'QFaceSwapper.help.model': {
                'en-US': 'File model dari folder atau tersedia untuk diunduh dari internet.\nAnda dapat melatih model sendiri di DeepFaceLab.'
            },
            'QFaceSwapper.swap_all_faces': {
                'en-US': 'Tukar Semua Wajah'
            },
            'QFaceSwapper.face_id': {
                'en-US': 'ID Wajah'
            },
            'QFaceSwapper.help.face_id': {
                'en-US': 'ID Wajah untuk ditukar.'
            },
            'QFaceSwapper.morph_factor': {
                'en-US': 'Faktor Morf'
            },
            'QFaceSwapper.help.morph_factor': {
                'en-US': 'Mengontrol tingkat morf wajah dari sumber ke selebriti.'
            },
            'QFaceSwapper.presharpen_amount': {
                'en-US': 'Pra-tajarkan'
            },
            'QFaceSwapper.help.presharpen_amount': {
                'en-US': 'Tajamkan gambar sebelum dimasukkan ke jaringan saraf.'
            },
            'QFaceSwapper.pregamma': {
                'en-US': 'Pra-gamma'
            },
            'QFaceSwapper.help.pregamma': {
                'en-US': 'Ubah gamma gambar sebelum dimasukkan ke jaringan saraf.'
            },
            'QFaceSwapper.postgamma': {
                'en-US': 'Pasca-gamma'
            },
            'QFaceSwapper.two_pass': {
                'en-US': 'Dua Kali Proses'
            },
            'QFaceSwapper.help.two_pass': {
                'en-US': 'Proses wajah dua kali. Mengurangi fps hingga setengahnya.'
            },
            'QFrameAdjuster.module_title': {
                'en-US': 'Penyesuai Bingkai'
            },
            'QFrameAdjuster.median_blur_per': {
                'en-US': 'Buram Median'
            },
            'QFrameAdjuster.help.median_blur_per': {
                'en-US': 'Buramkan seluruh bingkai menggunakan filter median.'
            },
            'QFrameAdjuster.degrade_bicubic_per': {
                'en-US': 'Degradasi Bikubik'
            },
            'QFrameAdjuster.help.degrade_bicubic_per': {
                'en-US': 'Degradasi seluruh bingkai menggunakan pengubahan ukuran bikubik.'
            },
            'QFaceMerger.module_title': {
                'en-US': 'Penggabung Wajah'
            },
            'QFaceMerger.face_x_offset': {
                'en-US': 'Offset X Wajah'
            },
            'QFaceMerger.face_y_offset': {
                'en-US': 'Offset Y Wajah'
            },
            'QFaceMerger.face_scale': {
                'en-US': 'Skala Wajah'
            },
            'QFaceMerger.face_mask_type': {
                'en-US': 'Jenis Masker Wajah'
            },
            'QFaceMerger.face_mask_erode': {
                'en-US': 'Erosi Masker Wajah'
            },
            'QFaceMerger.face_mask_blur': {
                'en-US': 'Buram Masker Wajah'
            },
            'QFaceMerger.help.color_transfer': {
                'en-US': 'Cocokkan distribusi warna wajah yang diganti dengan wajah asli.'
            },
            'QFaceMerger.color_transfer': {
                'en-US': 'Transfer Warna'
            },
            'QFaceMerger.interpolation': {
                'en-US': 'Interpolasi'
            },
            'QFaceMerger.color_compression': {
                'en-US': 'Kompresi Warna'
            },
            'QFaceMerger.face_opacity': {
                'en-US': 'Opasitas Wajah'
            },
            'QStreamOutput.module_title': {
                'en-US': 'Keluaran Streaming'
            },
            'QStreamOutput.avg_fps': {
                'en-US': 'FPS Rata-rata'
            },
            'QStreamOutput.help.avg_fps': {
                'en-US': 'FPS rata-rata dari aliran keluaran.'
            },
            'QStreamOutput.source_type': {
                'en-US': 'Sumber'
            },
            'QStreamOutput.show_hide_window': {
                'en-US': 'Jendela'
            },
            'QStreamOutput.aligned_face_id': {
                'en-US': 'ID Wajah'
            },
            'QStreamOutput.help.aligned_face_id': {
                'en-US': 'ID wajah yang disejajarkan untuk ditampilkan.'
            },
            'QStreamOutput.target_delay': {
                'en-US': 'Penundaan Target'
            },
            'QStreamOutput.help.target_delay': {
                'en-US': 'Penundaan target dalam milidetik antara bingkai masukan dan bingkai keluaran.\nCocokkan nilai ini dengan penundaan audio di perangkat lunak streaming Anda untuk mendapatkan aliran yang tersinkronisasi.'
            },
            'QStreamOutput.save_sequence_path': {
                'en-US': 'Simpan Sekuens'
            },
            'QStreamOutput.help.save_sequence_path': {
                'en-US': 'Simpan sekuens gambar dari aliran keluaran ke direktori.'
            },
            'QStreamOutput.save_fill_frame_gap': {
                'en-US': 'Isi Celah Bingkai'
            },
            'QStreamOutput.help.save_fill_frame_gap': {
                'en-US': 'Isi penurunan bingkai dengan menduplikasi bingkai terakhir.'
            },
            'QBCFrameViewer.title': {
                'en-US': 'Bingkai Sumber'
            },
            'QBCFaceAlignViewer.title': {
                'en-US': 'Wajah yang Disejajarkan'
            },
            'QBCFaceSwapViewer.title': {
                'en-US': 'Wajah yang Ditukar'
            },
            'QBCMergedFrameViewer.title': {
                'en-US': 'Bingkai yang Digabung'
            },
            'FileSource.image_folder': {
                'en-US': 'Folder Gambar'
            },
            'FileSource.video_file': {
                'en-US': 'File Video'
            },
            'FaceDetector.LARGEST': {
                'en-US': 'Terbesar'
            },
            'FaceDetector.DIST_FROM_CENTER': {
                'en-US': 'Jarak dari Pusat'
            },
            'FaceDetector.LEFT_RIGHT': {
                'en-US': 'Dari Kiri ke Kanan'
            },
            'FaceDetector.RIGHT_LEFT': {
                'en-US': 'Dari Kanan ke Kiri'
            },
            'FaceDetector.TOP_BOTTOM': {
                'en-US': 'Dari Atas ke Bawah'
            },
            'FaceDetector.BOTTOM_TOP': {
                'en-US': 'Dari Bawah ke Atas'
            },
            'FaceAligner.AlignMode.FROM_RECT': {
                'en-US': 'Dari Persegi Panjang'
            },
            'FaceAligner.AlignMode.FROM_POINTS': {
                'en-US': 'Dari Titik'
            },
            'FaceAligner.AlignMode.FROM_STATIC_RECT': {
                'en-US': 'Dari Persegi Panjang Statis'
            },
            'FaceSwapper.model_information': {
                'en-US': 'Informasi Model'
            },
            'FaceSwapper.filename': {
                'en-US': 'Nama File:'
            },
            'FaceSwapper.resolution': {
                'en-US': 'Resolusi:'
            },
            'FaceSwapper.downloading_model': {
                'en-US': 'Mengunduh Model...'
            },
            'StreamOutput.SourceType.SOURCE_FRAME': {
                'en-US': 'Bingkai Sumber'
            },
            'StreamOutput.SourceType.ALIGNED_FACE': {
                'en-US': 'Wajah yang Disejajarkan'
            },
            'StreamOutput.SourceType.SWAPPED_FACE': {
                'en-US': 'Wajah yang Ditukar'
            },
            'StreamOutput.SourceType.MERGED_FRAME': {
                'en-US': 'Bingkai yang Digabung'
            },
            'StreamOutput.SourceType.MERGED_FRAME_OR_SOURCE_FRAME': {
                'en-US': 'Bingkai yang Digabung atau Bingkai Sumber'
            },
            'StreamOutput.SourceType.SOURCE_N_MERGED_FRAME': {
                'en-US': 'Bingkai Sumber dan Bingkai yang Digabung'
            },
            'StreamOutput.SourceType.SOURCE_N_MERGED_FRAME_OR_SOURCE_FRAME': {
                'en-US': 'Bingkai Sumber dan Bingkai yang Digabung atau Bingkai Sumber'
            },
            'StreamOutput.SourceType.ALIGNED_N_SWAPPED_FACE': {
                'en-US': 'Wajah yang Disejajarkan dan Ditukar'
            }
        }
