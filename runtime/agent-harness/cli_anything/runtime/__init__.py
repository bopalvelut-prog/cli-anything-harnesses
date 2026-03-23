import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('runtime running')
@cli.command()
def start(): click.echo('runtime started')
if __name__ == '__main__': cli()
