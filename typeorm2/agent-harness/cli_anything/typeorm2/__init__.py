import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): click.echo('TypeORM migration')
if __name__ == '__main__': cli()
