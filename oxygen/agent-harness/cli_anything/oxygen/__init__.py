import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oxygen running')
@cli.command()
def start(): click.echo('oxygen started')
if __name__ == '__main__': cli()
