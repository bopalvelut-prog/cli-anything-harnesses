import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('upon running')
@cli.command()
def start(): click.echo('upon started')
if __name__ == '__main__': cli()
