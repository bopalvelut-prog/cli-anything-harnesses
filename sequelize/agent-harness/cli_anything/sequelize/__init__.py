import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): subprocess.run(['npx', 'sequelize-cli', 'db:migrate'])
@cli.command()
def seed(): subprocess.run(['npx', 'sequelize-cli', 'db:seed:all'])
if __name__ == '__main__': cli()
