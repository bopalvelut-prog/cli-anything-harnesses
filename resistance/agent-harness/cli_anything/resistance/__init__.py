import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resistance running')
@cli.command()
def start(): click.echo('resistance started')
if __name__ == '__main__': cli()
