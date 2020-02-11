oc-GNS3-lab : Automatisation du laboratoire de virtualisation GNS3/QEMU:
=====

Intro:
===

Dans le cadre du parcours AIC (Administrateur Infrastructure et Cloud) organisé par OpenClassroom, nous utilisons GNS3 couplé à QEMU/KVM. Pour chaque projet nécessitant une infrastructure virtualisée j'utilise une machine dédiée, qui est remise a 0 entre chaque projet pour disposer de la version la plus récente de GNS3.

But:
===

1. Mise en place des paramètres de base en partant d'Ubuntu Server 18.04 LTS
2. Installation et configuration de la suite de virtualisation Libvirt, ainsi que QEMU/KVM
3. Installation et configuration de GNS3
4. Tester le fonctionnement de GNS3 à travers son API et récupérer la version ça version
5. Si activé, installer la version de GNS3-Gui compatible avec le serveur sur notre machine client (Ubuntu 18.04/PopOS!)
6. ~~Importation des Appliances~~ -- Not working with gns3api
7. ~~Création d'une Infrastructure comprenant une Appliance "nat" reliée a un serveur CENTOS disposant de 2 cartes réseaux, et lui même relié à une machine client Fedora. -- Not working with gns3api since previous task can't~~


Fichier GNS3:
===

Nos appliances GNS3 (.gns3a) mise a jour son stockées sur notre gitlab : [[link | Ici]] et nos images Qemu sont présentes sur un nas local.




TODO:
===

- [x] Rédaction playbook général
- [x] Rédaction Roles individuel
- [ ] Debug docker support
- [ ] Rédaction Modules Python/GNS3
- [ ] Rédaction du playbook client



Technologie utilisé:
===

  - GNS3
  - [GNS3FY](https://github.com/dolew/gns3_py)
  - Ansible
  - Python 3
  - Ubuntu 18.04LTS Server
  - Docker-ce

  
