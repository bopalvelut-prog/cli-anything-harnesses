import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jruby running')
@cli.command()
def start(): click.echo('jruby started')
if __name__ == '__main__': cli()
