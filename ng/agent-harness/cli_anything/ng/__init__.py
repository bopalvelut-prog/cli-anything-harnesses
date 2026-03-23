import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ng running')
@cli.command()
def start(): click.echo('ng started')
if __name__ == '__main__': cli()
