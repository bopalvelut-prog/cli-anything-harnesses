import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stiff running')
@cli.command()
def start(): click.echo('stiff started')
if __name__ == '__main__': cli()
