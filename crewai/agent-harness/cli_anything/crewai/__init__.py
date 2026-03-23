import click
@click.group()
def cli(): pass
@cli.command()
def run(): click.echo('CrewAI run')
@cli.command()
def agents(): click.echo('CrewAI agents')
if __name__ == '__main__': cli()
