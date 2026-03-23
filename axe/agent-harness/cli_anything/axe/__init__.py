import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('axe running')
@cli.command()
def start(): click.echo('axe started')
if __name__ == '__main__': cli()
