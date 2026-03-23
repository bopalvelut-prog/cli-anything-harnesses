import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('garden running')
@cli.command()
def start(): click.echo('garden started')
if __name__ == '__main__': cli()
