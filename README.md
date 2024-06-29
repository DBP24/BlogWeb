# Creo nueva versión de mi Sitio web con Python - Django
# name project : web
# name apps : page, block, project, services
# Usando Django-material-dashboard 
    pip install django-material-dashboard
    python manage.py collectstatic
        # 'admin_material.apps.AdminMaterialDashboardConfig', configurations setting apps project
        # path('', include('admin_material.urls')), add urls  of project general
    pip install django-material

    INSTALLED_APPS = [
    ...
    'material',
            ...
        ]

        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
            os.path.join(BASE_DIR, 'static', 'django_material'),  # Asegúrate de incluir la carpeta de archivos estáticos de Django Material
        ]

# Información encontrada - WeBuilder


# Configuración Archivo media
    # pip install Pillow
    # En trabajo de Desarrollo:
    |Configuracion en urls - Setting del project:
        -----------------------------------
        if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        -------------------------------------------------
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# hacer un video en base a foto y audio -  analizar codigo 
#@markdown ##INICIAR V-Express<font size="5" color="purple"><br>PASO 1


import os
from google.colab import files

# Clonar el repositorio y configurar el entorno
%cd /content
!git clone -b dev https://github.com/camenduru/V-Express
%cd /content/V-Express

!apt -y install -qq aria2


model_urls = [
    "https://huggingface.co/camenduru/V-Express/resolve/main/insightface_models/models/buffalo_l/1k3d68.onnx",
    "https://huggingface.co/camenduru/V-Express/resolve/main/insightface_models/models/buffalo_l/2d106det.onnx",
    "https://huggingface.co/camenduru/V-Express/resolve/main/insightface_models/models/buffalo_l/det_10g.onnx",
    "https://huggingface.co/camenduru/V-Express/resolve/main/insightface_models/models/buffalo_l/genderage.onnx",
    "https://huggingface.co/camenduru/V-Express/resolve/main/insightface_models/models/buffalo_l/w600k_r50.onnx",
    "https://huggingface.co/camenduru/V-Express/raw/main/sd-vae-ft-mse/config.json",
    "https://huggingface.co/camenduru/V-Express/resolve/main/sd-vae-ft-mse/diffusion_pytorch_model.bin",
    "https://huggingface.co/camenduru/V-Express/raw/main/stable-diffusion-v1-5/unet/config.json",
    "https://huggingface.co/camenduru/V-Express/resolve/main/v-express/audio_projection.pth",
    "https://huggingface.co/camenduru/V-Express/resolve/main/v-express/denoising_unet.pth",
    "https://huggingface.co/camenduru/V-Express/resolve/main/v-express/motion_module.pth",
    "https://huggingface.co/camenduru/V-Express/resolve/main/v-express/reference_net.pth",
    "https://huggingface.co/camenduru/V-Express/resolve/main/v-express/v_kps_guider.pth",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/config.json",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/feature_extractor_config.json",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/preprocessor_config.json",
    "https://huggingface.co/camenduru/V-Express/resolve/main/wav2vec2-base-960h/pytorch_model.bin",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/special_tokens_map.json",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/tokenizer_config.json",
    "https://huggingface.co/camenduru/V-Express/raw/main/wav2vec2-base-960h/vocab.json"
]

for url in model_urls:
    !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {url} -d /content/V-Express/model_ckpts/$(dirname {url.split('/main/')[1]}) -o $(basename {url})

!pip install diffusers==0.24.0 imageio-ffmpeg==0.4.9 insightface==0.7.3 omegaconf==2.2.3 onnxruntime==1.16.3 safetensors==0.4.2 transformers==4.30.2 einops==0.4.1 tqdm==4.66.1 xformers==0.0.26.post1 av accelerate


os.makedirs('/content/V-Express/test_samples/prueba', exist_ok=True)


uploaded = files.upload()


for filename in uploaded.keys():
    dest_path = os.path.join('/content/V-Express/test_samples/prueba', filename)
    os.rename(filename, dest_path)


image_path = [os.path.join('/content/V-Express/test_samples/prueba', f) for f in uploaded.keys() if f.endswith(('.jpg', '.jpeg', '.png'))][0]
audio_path = [os.path.join('/content/V-Express/test_samples/prueba', f) for f in uploaded.keys() if f.endswith(('.mp3', '.wav'))][0]


!python /content/V-Express/inference.py \
    --reference_image_path {image_path} \
    --audio_path {audio_path} \
    --kps_path "/content/V-Express/test_samples/short_case/10/kps.pth" \
    --output_path "/content/V-Express/output/short_case/resultado.mp4" \
    --retarget_strategy "no_retarget" \
    --num_inference_steps 25


files.download('/content/V-Express/output/short_case/resultado.mp4')