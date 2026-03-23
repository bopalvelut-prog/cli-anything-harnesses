import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scanner running')
@cli.command()
def start(): click.echo('scanner started')
if __name__ == '__main__': cli()
