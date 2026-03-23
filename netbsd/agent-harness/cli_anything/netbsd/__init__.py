import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('netbsd running')
@cli.command()
def start(): click.echo('netbsd started')
if __name__ == '__main__': cli()
