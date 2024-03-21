# La base de la imagen
FROM python:3.9.19

# Directorio del trabajo
WORKDIR /app

# Copiar el erchivo requirements.txt en el contenedor
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Exponer el puerto 8000 para que la apliación pueda ser accedida desde afuera del contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "mobiera/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]