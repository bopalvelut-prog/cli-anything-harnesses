import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('AutoGen chat')
@cli.command()
def agents(): click.echo('AutoGen agents')
if __name__ == '__main__': cli()
