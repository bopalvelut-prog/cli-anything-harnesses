import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['./mvnw', 'spring-boot:run'])
@cli.command()
def build(): subprocess.run(['./mvnw', 'package'])
if __name__ == '__main__': cli()
