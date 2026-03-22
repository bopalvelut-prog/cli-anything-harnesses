import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): subprocess.run(['npx', 'knex', 'migrate:latest'])
@cli.command()
def seed(): subprocess.run(['npx', 'knex', 'seed:run'])
if __name__ == '__main__': cli()
