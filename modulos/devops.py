from modulos.inteligencia import normalizar


def detectar_devops(texto):
    texto = normalizar(texto)

    temas = {

        "docker": {
            "keys": [
                "docker",
                "contenedor",
                "contenedores",
                "imagen docker",
                "dockerfile",
                "docker compose",
            ],
            "titulo": "Docker",
            "respuesta": """Docker permite ejecutar aplicaciones en contenedores aislados.

Comandos principales:

• Construir imagen
docker build -t mi-app .

• Ejecutar contenedor
docker run -d -p 80:80 mi-app

• Ver contenedores
docker ps

• Ver todos
docker ps -a

• Detener
docker stop <id>

• Eliminar
docker rm <id>

• Eliminar imagen
docker rmi <imagen>

• Docker Compose
docker compose up -d
docker compose down

Buenas prácticas

• Utilizar imágenes oficiales.
• Usar multistage builds.
• Evitar ejecutar como root.
• Reducir el tamaño de la imagen.
• Usar archivos .dockerignore.
• Mantener versiones fijas.
"""
        },

        "kubernetes": {
            "keys": [
                "kubernetes",
                "k8s",
                "kubectl",
                "pod",
                "deployment",
                "service",
            ],
            "titulo": "Kubernetes",
            "respuesta": """Kubernetes administra contenedores en producción.

Comandos útiles

kubectl get pods

kubectl get deployments

kubectl describe pod <nombre>

kubectl logs <pod>

kubectl apply -f archivo.yaml

kubectl delete pod <pod>

kubectl rollout restart deployment/<deployment>

Buenas prácticas

• Mantener los pods pequeños.
• Configurar readiness y liveness probes.
• Limitar CPU y memoria.
• Utilizar ConfigMaps y Secrets.
• No guardar información sensible en imágenes.
"""
        },

        "cicd": {
            "keys": [
                "ci",
                "cd",
                "ci/cd",
                "pipeline",
                "github actions",
                "gitlab ci",
                "azure devops",
                "integracion continua",
                "despliegue continuo",
            ],
            "titulo": "CI/CD",
            "respuesta": """CI/CD automatiza la compilación, pruebas y despliegue.

Flujo recomendado

1. Compilar.
2. Ejecutar pruebas.
3. Analizar calidad.
4. Construir artefacto.
5. Desplegar automáticamente.
6. Verificar.
7. Rollback si existe error.

Buenas prácticas

• Nunca guardar secretos en Git.
• Ejecutar pruebas automáticas.
• Automatizar despliegues.
• Versionar artefactos.
• Implementar rollback.
"""
        },

        "jenkins": {
            "keys": [
                "jenkins"
            ],
            "titulo": "Jenkins",
            "respuesta": """Jenkins automatiza pipelines.

Pipeline básico

Checkout

↓

Build

↓

Test

↓

Package

↓

Deploy

Buenas prácticas

• Utilizar Jenkinsfile.
• Dividir pipelines.
• Mantener agentes separados.
• Versionar el Jenkinsfile.
"""
        },

        "linux": {
            "keys": [
                "linux",
                "ubuntu",
                "debian",
                "centos",
                "bash",
                "terminal",
            ],
            "titulo": "Linux",
            "respuesta": """Comandos frecuentes

pwd

ls -la

cd carpeta

mkdir proyecto

rm -rf carpeta

cp archivo destino

mv origen destino

chmod +x archivo

top

htop

df -h

free -h

systemctl status servicio
"""
        },

        "nginx": {
            "keys": [
                "nginx"
            ],
            "titulo": "NGINX",
            "respuesta": """NGINX funciona como servidor web y reverse proxy.

Comandos

sudo systemctl start nginx

sudo systemctl restart nginx

sudo systemctl status nginx

sudo nginx -t

Buenas prácticas

• Activar HTTPS.
• Configurar compresión Gzip.
• Mantener certificados actualizados.
"""
        },

        "apache": {
            "keys": [
                "apache",
                "httpd"
            ],
            "titulo": "Apache",
            "respuesta": """Servidor web Apache.

Comandos

systemctl start apache2

systemctl restart apache2

apachectl configtest

Buenas prácticas

• Deshabilitar módulos innecesarios.
• Utilizar HTTPS.
• Configurar VirtualHost.
"""
        },

        "ssh": {
            "keys": [
                "ssh",
                "openssh",
                "llave ssh",
                "clave ssh",
            ],
            "titulo": "SSH",
            "respuesta": """SSH permite administrar servidores remotamente.

Generar llave

ssh-keygen -t ed25519

Agregar llave

ssh-add ~/.ssh/id_ed25519

Conectar

ssh usuario@ip

Copiar archivos

scp archivo usuario@ip:/ruta

Buenas prácticas

• Deshabilitar login root.
• Utilizar llaves SSH.
• Cambiar puerto cuando sea necesario.
• Mantener permisos correctos.
"""
        },

        "terraform": {
            "keys": [
                "terraform"
            ],
            "titulo": "Terraform",
            "respuesta": """Terraform permite administrar infraestructura como código.

Comandos

terraform init

terraform validate

terraform plan

terraform apply

terraform destroy

Buenas prácticas

• Versionar estado remoto.
• Utilizar módulos.
• No modificar recursos manualmente.
"""
        },

        "ansible": {
            "keys": [
                "ansible"
            ],
            "titulo": "Ansible",
            "respuesta": """Ansible automatiza configuración de servidores.

Comandos

ansible all -m ping

ansible-playbook playbook.yml

Buenas prácticas

• Usar inventarios.
• Dividir roles.
• Mantener playbooks reutilizables.
"""
        },

        "git": {
            "keys": [
                "git",
                "github",
                "gitlab",
            ],
            "titulo": "Git",
            "respuesta": """Flujo recomendado

git status

git add .

git commit -m "mensaje"

git pull

git push

Buenas prácticas

• Commits pequeños.
• Usar ramas.
• Pull antes de push.
• Resolver conflictos correctamente.
"""
        },
    }

    for tema in temas.values():
        if any(k in texto for k in tema["keys"]):
            return tema["titulo"], tema["respuesta"]

    return None
