# Tutorials-ElectronApp
A collection of **Hello World** tutorials of desktop apps built with Electron



👉 How to run the desktop-app:
```
cd 1_HelloWorld 
npm run dev  
```

👉 How to run the web-app:
```
cd 2_HelloWorld_web 
npm run dev  
```
and open your  ➜ Local: http://localhost:****/   

or start the server and open the app in a new browser tab 
```
npm run dev -- --open
````




# Getting started with electron-vite




👉 [**Electron-vite**](https://electron-vite.org/) is a build tool that aims to provide a faster and leaner development experience for Electron.

👉 [**The Electron framework**](https://www.electronjs.org/es/) lets you write cross-platform desktop applications using JavaScript, HTML and CSS. It is based on Node.js and Chromium and is used by the Visual Studio Code and many other apps.

👉 [**Vite**](https://vitejs.dev/) (French word for "quick", pronounced /vit/, like "veet") is a build tool that aims to provide a faster and leaner development experience for modern web projects. It consists of two major parts:

👉 [**Svelte**](https://svelte.dev/) is a new way to build web applications. It's a compiler that takes your declarative components and converts them into efficient JavaScript that surgically updates the DOM.



## 1. Electron-vite pre-requisites:
>Requires Node.js version 14.18+ and Vite version 3.0+

Just install the [Node.js package](https://nodejs.org/en), it includes both node and npm executables

Vite is resolved within the create-electron tool, no steps required.


## 2. Scaffolding Your First electron-vite DesktopApp Project:
use the create-electron tool to scaffold your project:


>👉 npm create @quick-start/electron


Then follow the prompts!


>✔ Project name: ...electron-vite-app_svelte  (usar solo letras minusculas, no espacios)
✔ Select a framework: ›... [svelte](https://svelte.dev/)  
✔ Add TypeScript? … [No]() / Yes  
✔ Add Electron updater plugin? … No / [Yes]()  
✔ Enable Electron download mirror proxy? … No / [Yes]()  

Scaffolding project in ./electron-app_svelte...  
Done.  

See [create-vite](https://github.com/alex8088/quick-start/tree/master/packages/create-electron) for more details on each supported template

Currently supported template presets include:

| JavaScript   |   TypeScript  |    
|--------------|:-------------:|
| vanilla      | vanilla-ts    |
| vue          | vue-ts        |   
| react        | react-ts      |   
| svelte       | svelte-ts     |   
| solid        | solid-ts      |    









# 3. Scaffolding Your First Vite-Svelte WebApp Project:


Tambien puedes usar [Vite](https://v3.vitejs.dev/guide/) para crear plantillas de proyectos Web.

Use Vite's official create command:

 >👉 npm create vite@latest my-vite-project_svelte


# 4. Resources


>[**electron**](https://www.electronjs.org/es/)


>[**svelte**](https://svelte.dev/)
>[ui-library](https://madewithsvelte.com/ui-library)


>[react](https://es.react.dev/)

>[tailwind](https://tailwindcss.com/)

>[vite](https://v3.vitejs.dev/guide/)

