import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('finance running')
@cli.command()
def start(): click.echo('finance started')
if __name__ == '__main__': cli()
