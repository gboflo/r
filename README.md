# vpm-sample-packages

Some package examples for the Velocity Package Manager (VPM) effort.

Each sample package should be in a new branch.

# Steps to create example-0.
1. Create example-0 branch in project.
2. Make one or more automation asset projects (I already had scripts, sleep0,1,2 so just copied them.) Make sure they have a
manifest or a ".project" file so they are recognized as projects.
3. Download driver projects using repository service API. Expand and save in first-level folders in package.
4. Create runlists in Velocity. Download and copy to git repository. I put them in the "runlists" folder but they can go anywhere, even in different folders.
5. Create resources.
    1. Velocity, Velocity Cluster, VDS, VDS-0, VDS-1, and VDS-2.
    2. Physically connect Velocity and VDS.
    3. Physically connect Velocity Cluster to VDS-0, VDS-1, and VDS-2.
    4. Export all to a zip file.
    5. Expand zip file to a folder. I put in "InventoryA".
6. Create topologies.
    1. Velocity_Single_VDS with Velocity and VDS.
    2. Velocity_VDS_Cluster with Velocity Cluster, VDS-0, VDS-1, and VDS-2.
    3. Export topologies.
    4. We are supposed to be able to include topologies in an inventory zip but I don't know how to do that. So I just put them in "InventoryA"
7. Use reporting service API to download report templates. Copy to git repository. They can go anywhere. I put in the "reports" folder along with Kibana data.
8. Use Kibana to create dashboards and vizualization and export to JSON. Copy to git repository and give "kibana" extension. They also can go anywhere. I put them in the "reports" folder.
