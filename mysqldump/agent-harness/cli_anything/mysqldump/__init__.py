import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mysqldump running')
@cli.command()
def start(): click.echo('mysqldump started')
if __name__ == '__main__': cli()
