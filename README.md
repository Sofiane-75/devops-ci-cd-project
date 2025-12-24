# DevOps CI/CD Project

Ce projet met en place une chaîne CI/CD simple et reproductible pour une application FastAPI conteneurisée.  
L’objectif est de disposer d’un pipeline clair, automatisé, et facile à comprendre pour un environnement de développement local.

## Contenu du projet

- Une application FastAPI minimale (répertoire `app/`)
- Un Dockerfile pour construire l’image
- Un pipeline GitHub Actions pour :
  - construire l’image Docker
  - analyser l’image avec Trivy
  - pousser l’image sur Docker Hub
  - créer un tag versionné basé sur le numéro de run
- Des manifestes Kubernetes (`k8s/`) pour un déploiement local via k3d

## Pipeline CI/CD

Le pipeline se déclenche à chaque push sur la branche `main`.  
Il exécute les étapes suivantes :

1. Build de l’image Docker
2. Scan de sécurité avec Trivy
3. Push de l’image sur Docker Hub (`sofianedevops/devops-app`)
4. Création d’un tag versionné (`v1`, `v2`, etc.)

Le déploiement Kubernetes n’est pas exécuté dans GitHub Actions, car le cluster k3d est local et n’est pas accessible depuis l’extérieur.  
Le déploiement se fait donc manuellement en local.

## Déploiement local (k3d)

Créer un cluster k3d avec exposition du NodePort :

```bash
k3d cluster create --port "30080:30080@server:0"
```

Déployer l’application :

```bash
kubectl apply -f k8s/
```

Vérifier que les ressources sont en place :

```bash
kubectl get pods
kubectl get svc
```

Accéder à l’application :

```bash
curl http://localhost:30080
```

Réponse attendue :

```json
{"message":"Azul, c'est Sofiane !"}
```

## Structure du dépôt

```
.
├── app/
│   ├── main.py
│   └── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── .github/workflows/ci.yml
```

## Objectif du projet

Ce projet sert de base pour illustrer un workflow DevOps complet en environnement local : 
construction d’image, analyse, publication, versionnement et déploiement Kubernetes. 
