#!/bin/bash

# kurbeScript.sh — Setup and verify local Kubernetes cluster using Minikube

echo "🚀 Starting Kubernetes cluster setup..."

# Check if Minikube is installed
if ! command -v minikube &> /dev/null
then
    echo "❌ Minikube is not installed."
    echo "🔧 Installing Minikube..."

    # Detect OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
        sudo install minikube-linux-amd64 /usr/local/bin/minikube
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install minikube
    else
        echo "⚠️ Unsupported OS. Please install Minikube manually from https://minikube.sigs.k8s.io/docs/start/"
        exit 1
    fi
else
    echo "✅ Minikube is already installed."
fi

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null
then
    echo "❌ kubectl not found. Installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt-get update -y
        sudo apt-get install -y kubectl
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install kubectl
    else
        echo "⚠️ Unsupported OS. Please install kubectl manually from https://kubernetes.io/docs/tasks/tools/"
        exit 1
    fi
else
    echo "✅ kubectl is already installed."
fi

# Start Minikube cluster
echo "🟢 Starting Minikube cluster..."
minikube start --driver=docker

# Verify cluster info
echo "🔍 Verifying Kubernetes cluster..."
kubectl cluster-info

# List all pods in all namespaces
echo "📦 Retrieving available pods..."
kubectl get pods --all-namespaces

echo "🎉 Kubernetes cluster is up and running successfully!"
