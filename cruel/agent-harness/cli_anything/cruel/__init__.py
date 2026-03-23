import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cruel running')
@cli.command()
def start(): click.echo('cruel started')
if __name__ == '__main__': cli()
