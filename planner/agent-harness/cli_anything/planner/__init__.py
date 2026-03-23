import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('planner running')
@cli.command()
def start(): click.echo('planner started')
if __name__ == '__main__': cli()
