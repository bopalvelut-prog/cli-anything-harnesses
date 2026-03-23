import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('linters running')
@cli.command()
def start(): click.echo('linters started')
if __name__ == '__main__': cli()
