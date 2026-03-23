import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sure running')
@cli.command()
def start(): click.echo('sure started')
if __name__ == '__main__': cli()
