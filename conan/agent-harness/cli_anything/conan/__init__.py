import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('conan running')
@cli.command()
def start(): click.echo('conan started')
if __name__ == '__main__': cli()
