import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('LangChain chat')
@cli.command()
def agents(): click.echo('LangChain agents')
if __name__ == '__main__': cli()
