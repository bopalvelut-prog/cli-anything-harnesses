import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ripple running')
@cli.command()
def start(): click.echo('ripple started')
if __name__ == '__main__': cli()
