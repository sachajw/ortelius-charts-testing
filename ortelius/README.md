# 

[]() - 

## TL;DR;

```bash
$ helm repo add  
$ helm repo update
$ helm search repo /ortelius --version=10.0.122
$ helm upgrade -i  /ortelius -n  --create-namespace --version=10.0.122
```

## Introduction

This chart deploys  on a [Kubernetes](http://kubernetes.io) cluster using the [Helm](https://helm.sh) package manager.

## Prerequisites


## Installing the Chart

To install/upgrade the chart with the release name ``:

```bash
$ helm upgrade -i  /ortelius -n  --create-namespace --version=10.0.122
```

The command deploys  on the Kubernetes cluster in the default configuration. The [configuration](#configuration) section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall the ``:

```bash
$ helm uninstall  -n 
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the `ortelius` chart and their default values.

|           Parameter            | Description |      Default       |
|--------------------------------|-------------|--------------------|
| global.postgresql.enabled      |             | <code>false</code> |
| global.nginxController.enabled |             | <code>false</code> |


Specify each parameter using the `--set key=value[,key=value]` argument to `helm upgrade -i`. For example:

```bash
$ helm upgrade -i  /ortelius -n  --create-namespace --version=10.0.122 --set 
```

Alternatively, a YAML file that specifies the values for the parameters can be provided while
installing the chart. For example:

```bash
$ helm upgrade -i  /ortelius -n  --create-namespace --version=10.0.122 --values values.yaml
```
