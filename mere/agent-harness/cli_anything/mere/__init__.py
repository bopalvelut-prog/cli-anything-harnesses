import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mere running')
@cli.command()
def start(): click.echo('mere started')
if __name__ == '__main__': cli()
