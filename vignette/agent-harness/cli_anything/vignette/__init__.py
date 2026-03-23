import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vignette running')
@cli.command()
def start(): click.echo('vignette started')
if __name__ == '__main__': cli()
