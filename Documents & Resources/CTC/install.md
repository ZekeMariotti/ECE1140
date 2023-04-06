# Installing and Running

## Backend
A binarized version of the backend is available at `src/CTC/ctc-backend/main`. You will need to copy the following files into a new directory:
> main.exe  
> greenLineBlocks.csv  
> greenLineSwitches.csv  
> redLineBlocks.csv  
> redLineSwitches.csv  

Once the above files are extracted into a new folder, you can run the backend by opening a terminal and running `main.exe`

## Frontend
Before installing the frontend, you must download a webserver. For this guide, we will be using NGINX.

First download NGINX from the following link:
> https://nginx.org/download/nginx-1.22.1.zip

Then extract it to a folder. Next we will copy the files needed over from the built binaries. Navigate to `src/CTC/ctc-frontend/dist/ctc-frontend` and copy all of those files to the extracted NGINX folder's `/html` directory. Replace files if prompted.

We will need to make one configuration change to the NGINX config to support Angular web applications (such as this one). Angular has it's own routing module built into it, so we need to tell NGINX to foward all routes to the same html and let Angular handle it. We do this by modifying line 46 of `/conf/nginx.conf` in the nginx file to add `try_files $uri $uri/ /index.html;`. Lines 43-47 of `/conf/nginx.conf` should now read as the following:  
```conf
location / {
    root   html;
    index  index.html index.htm;
    try_files $uri $uri/ /index.html; # This line is new
}
```
To start the web server, we just need to run `nginx.exe` in the main directory of the extract nginx package.