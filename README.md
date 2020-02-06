oc-GNS3-lab : Automatisation du laboratoire de virtualisation GNS3/QEMU:
=====

Intro:
===

Dans le cadre du parcours AIC (Administrateur Infrastructure et Cloud) organisé par OpenClassroom, nous utilisons GNS3 couplé à QEMU/KVM. Pour chaque projet nécessitant une infrastructure virtualisé j'utilise une machine dédier, qui est remise a 0 entre chaque projet pour disposé de la version la plus récente de GNS3.

But:
===

1. Mise en place des paramètres de base en partant d'Ubuntu Server 18.04 LTS
2. Installation et configuration de la suite de virtualisation Libvirt, ainsi que QEMU/KVM
3. Installation et configuration de GNS3
4. Importation des Appliances
5. Création d'une Infrastructure comprenant un Appliances "nat" relié a un serveur CENTOS disposant de 2 carte réseau, et lui même relié à une machine clients Fedora.


Fichier GNS3:
===

Nos appliances GNS3 (.gns3a) mise a jour son stocker sur notre gitlab : [[link | Ici]] et nos image Qemu son présente sur un nas local.




TODO:
===

- [ ] Rédaction playbook général
- [ ] Rédaction Roles individuel
- [ ] Rédaction Modules Python/GNS3



Technologie utilisé:
===

  - GNS3
  - [[https://github.com/dolew/gns3_py | GNS3FY ]]
  - Ansible