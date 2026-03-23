import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('uninstall running')
@cli.command()
def start(): click.echo('uninstall started')
if __name__ == '__main__': cli()
