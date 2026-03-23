import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('llamacpp running')
@cli.command()
def start(): click.echo('llamacpp started')
if __name__ == '__main__': cli()
