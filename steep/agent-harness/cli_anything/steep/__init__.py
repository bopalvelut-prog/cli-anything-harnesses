import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('steep running')
@cli.command()
def start(): click.echo('steep started')
if __name__ == '__main__': cli()
