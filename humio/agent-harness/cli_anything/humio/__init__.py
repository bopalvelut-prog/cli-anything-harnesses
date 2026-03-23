import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('humio running')
@cli.command()
def start(): click.echo('humio started')
if __name__ == '__main__': cli()
