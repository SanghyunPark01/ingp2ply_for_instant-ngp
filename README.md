# ingp to ply converter
InstantNGP saves snapshot as .ingp, this repo makes .ingp into .ply (point cloud)

## How to use  

**First**, Clone this repository **in your instant-ngp directory**
```
cd instant-ngp
git clone https://github.com/SanghyunPark01/ingp2ply_for_instant-ngp.git
```  
**And then**,  
* Modify the file path  
`ingp2ply.py` : `ingp_path`, `output_ply_name`  
`test.py` : `pcd_path`
* Modify the Resolution  
  `ingp2ply.py` : `resolution`  

## Test  
```
python ingp2ply.py
python test.py
```