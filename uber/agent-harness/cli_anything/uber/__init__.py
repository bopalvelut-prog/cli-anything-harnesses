import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uber running')
@cli.command()
def start(): click.echo('uber started')
if __name__ == '__main__': cli()
