% % 
% 
clear all
clc
% %%%%select the diameter of the hole
dia = 1.2;
 N = 1; %%% number of simulations %%750
a11 = 400*(0.1);
a12= 160*(0.1);
%%%%start and end of x and y co-ordinates
xms=a11/2;%10.5*dia;
xmf=a11/2 + 2*(dia);%14.5*dia;
yms=a12/2;%dia*3;
ymf=a12/2 + 2*(dia);%dia*7;
%%%% meshgrid  for interpolation
g = 0.085;
xq1=xms:g:xmf;
%xq2=a11/2-1.5*dia/2:g:a11/2+1.5*dia/2;
%xq3=a11/2+1.5*dia/2:g:xmf;
xq = xq1';
yq1=ymf:-1*g:yms;
%yq2=a12/2-1.5*dia/2:g:a12/2+1.5*dia/2;
%yq3=a12/2+1.5*dia/2:g:ymf;
yq = yq1';
[K1,K2] = meshgrid(xq, yq);
a= size(xq1,2);
b= size(yq1,2);
for k = 1:a
    for j=1:b
       e=((k*g - 0))^2+((j*g - 2*dia))^2-(.5*dia)^2;
        if e<0
            K1(j,k)=  NaN;
            K2(j,k)=  NaN;
        end
    end
end
 zz1=0;
 zz2= 0;
disp("ddaf")
%%%%input xx,yy,elst value of all simulations
for i =1:N
    fx =[ 'C:\Users\Athiest69\Desktop\PROJECT\9.5D\x' num2str(i) '.txt'];  %%% add path of xx yy u1 u2 values
    fy =[ 'C:\Users\Athiest69\Desktop\PROJECT\9.5D\y' num2str(i) '.txt'];
    fu =[ 'C:\Users\Athiest69\Desktop\PROJECT\9.5D\u1' num2str(i) '.txt'];
    fv =[ 'C:\Users\Athiest69\Desktop\PROJECT\9.5D\u2' num2str(i) '.txt'];
    
x = textfile(fx);
y = textfile(fy);
z1 = textfile(fu);
z2 = textfile(fv);
U1 = griddata(x,y,z1,K1,K2);   %%  interpolation over the grid 
U2 = griddata(x,y,z2,K1,K2);


zz1 = U1+zz1;
 zz2 = U2+zz2;
i  ;
end
  %%%  avg of disp values
znk1 = (zz1)./N;
znk2 = (zz2)./N;
%% saving data 
 xlswrite('znk1.xlsx',znk1);
 xlswrite('znk2.xlsx',znk2);
E = zeros(2*(size(K1,1)-1),2*(size(K1,1)-1));
%%% calculation of strain  using strain mapping 
       for j = 1: (size(K1,1)-1)
    for i = 1: (size(K1,1)-1)
      
       
        
    
         v = [znk1(j,i);znk2(j,i);znk1(j,i+1);znk2(j,i+1);znk1(j+1,i+1);znk2(j+1,i+1);znk1(j+1,i);znk2(j+1,i)];
        e1= strain1(v);
        e2= strain2(v);
        e3= strain3(v);
        e4= strain4(v);
       E((2*j-1),(2*i-1)) = e1(1); %E(i,1);
        E((2*j-1),2*i) = e2(1); %+E(i+1,1);
        E(2*j,(2*i-1)) = e4(1); % +E(i+size(K1,1),1);
        E(2*j,2*i) = e3(1);
      
        
    end
       end  
       
   %% ne is normalised strain 
   su = round(2.4/g)+1;
   %se = 2*(su -1);
   r = E((((2*su-2)- round(1.2/g)-2):-1:1),1);
   %p = E((((su-1)- round(40/g)):-1:1),(su));
   %p = E((300:-1:1),402);
   %r = E((300:-1:1),403);
   %l = (p + r)./(24*(10)^(-5));
   st = (r)./(7.5*(10)^(-4));
   %R = zm1(303:-1:1,402);
   %k = linspace(0,4,40);
    m = g*(size(r)-1);
    H = 0:g:(m);
    h = H./1.2;
    
     
      
  plot(h,st)
  
  xlim([0 1.5])
  xlabel("X2/d",'fontsize',12)
  ylabel("Normalised Strain along vertical path", 'fontsize',12)
 % title("GS = 0.085 NS=300 mesh 0.035",'fontsize',11)
  legend("d/w = 1;NS 750; MR 1000")

function E1 = strain1(v)
B1 = [1 0 0 0;0 0 0 1;0 1 1 0];
%% for node 1 
x1=-1/sqrt(3);eta1=-1/sqrt(3);
B21 = B2();
B31 = B3(x1,eta1);
B12 = B1*B21;
B = B12*B31;
E1 =B*v; 
end 
function E1 = strain2(v)
B1 = [1 0 0 0;0 0 0 1;0 1 1 0];
%% for node 1 
x1=1/sqrt(3);eta1=-1/sqrt(3);
B21 = B2();
B31 = B3(x1,eta1);
B12 = B1*B21;
B = B12*B31;
E1 =B*v; 
end 
function E1 = strain3(v)
B1 = [1 0 0 0;0 0 0 1;0 1 1 0];
%% for node 1 
x1=1/sqrt(3);eta1=1/sqrt(3);
B21 = B2();
B31 = B3(x1,eta1);
B12 = B1*B21;
B = B12*B31;
E1 =B*v; 
end 
function E1 = strain4(v)
B1 = [1 0 0 0;0 0 0 1;0 1 1 0];
%% for node 4
x1=-1/sqrt(3);eta1=1/sqrt(3);
B21 = B2();
B31 = B3(x1,eta1);
B12 = B1*B21;
B = B12*B31;
E1 =B*v; 
end 


function B21 = B2()
B21 = [0.05/0.0025 0 0 0;0 0.05/0.0025 0 0;0 0 0.05/0.0025 0;0 0 0 0.05/0.0025];
end 
function B31 = B3(x1,eta1)
B31 = [-(1-eta1)*0.25 0 (1-eta1)*0.25 0 (1+eta1)*0.25 0 -(1+eta1)*0.25 0;...
       -(1-x1)*0.25 0  -(1+x1)*0.25 0 (1+x1)*0.25 0 (1-x1)*0.25 0;...
       0 -(1-eta1)*0.25 0 (1-eta1)*0.25 0 (1+eta1)*0.25 0 -(1+eta1)*0.25;...
       0  -(1-x1)*0.25 0  -(1+x1)*0.25 0 (1+x1)*0.25 0 (1-x1)*0.25];
end
function value = textfile(path)
    fileID = fopen(path,'r'); 
    value= fscanf(fileID,'%f');
    fclose(fileID);
end